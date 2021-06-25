import dask
import pandas as pd
import sklearn.manifold

import credit.embeddings.bijections
import credit.embeddings.reference


class Representations:

    def __init__(self, blob: pd.DataFrame):
        """

        :param blob:
        """

        # Data
        self.blob = blob

        # Instances
        self.reference = credit.embeddings.reference.Reference()
        self.t_sne = sklearn.manifold.TSNE(
            n_components=2, perplexity=50.0, early_exaggeration=12.0, learning_rate=200.0,
            n_iter=1000, n_iter_without_progress=500, metric='cosine', init='pca', random_state=5, method='exact')

    @dask.delayed
    def __excerpt(self, values: list) -> pd.DataFrame:
        """

        :param values:
        :return:
        """

        return self.blob[values]

    @dask.delayed
    def __transformations(self, excerpt: pd.DataFrame) -> pd.DataFrame:
        """

        :param excerpt:
        :return:
        """

        transformation = self.t_sne.fit_transform(X=excerpt)
        transformation_ = pd.DataFrame(data=transformation, columns=['tsne_1', 'tsne_2'])

        return pd.concat((excerpt, transformation_), axis=1)

    @dask.delayed
    def __reference(self, transformations: pd.DataFrame, values: list):
        """

        :param transformations:
        :param values:
        :return:
        """

        return self.reference.exc(features=values, patterns=transformations)

    @dask.delayed
    def __remap(self, excerpt: pd.DataFrame, reference: dict, key: str):
        """

        :param excerpt:
        :param reference:
        :param key:
        :return:
        """

        return credit.embeddings.bijections.Bijections(
            reference=reference, key=key).exc(blob=excerpt)

    def exc(self, groups: dict):
        """

        :param groups:
        :return:
        """

        computations = []
        for key, values in groups.items():
            # Excerpt
            excerpt = self.__excerpt(values=values)

            # T-SNE Transform
            transformations = self.__transformations(excerpt=excerpt)

            # The dictionary of mappings for 'key', hence ascertaining a
            # bijective relationship between the features of 'key' & T-SNE values
            reference = self.__reference(transformations=transformations, values=values)

            # Hence, a clean mapping between features & embeddings
            frame = self.__remap(excerpt=excerpt, reference=reference, key=key)

            # Hence
            computations.append((frame, reference, key))

        dask.visualize(computations, filename='computations', format='pdf')
        representations = dask.compute(computations, scheduler='processes')[0]

        return representations
