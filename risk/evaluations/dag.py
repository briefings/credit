"""Module dag"""

import os

import graphviz
import pymc3


class DAG:
    """
    Class DAG
    """

    def __init__(self):
        """
        The constructor

        """

    @staticmethod
    def exc(model: pymc3.Model, directory: str):
        """

        :param model:
        :param directory:
        :return:
        """

        # The DAG
        diagram = pymc3.model_graph.ModelGraph(model=model).make_graph()
        diagram.node_attr.update(shape='circle')
        diagram.graph_attr.update(size="11.3,11.9")

        # Diagrams
        diagram.save(os.path.join(directory, 'model.gv'))
        graphviz.render(engine='dot', format='pdf', filepath=os.path.join(directory, 'model.gv'))

        return graphviz.Source.from_file(filename=os.path.join(directory, 'model.gv'))
