import pickle
import pymc3
import zipfile
import os


class Assets:

    def __init__(self, directory: str):
        """

        """

        self.directory = directory

    def pocket_(self, pocket: dict):

        pickled = pickle.dumps(pocket)
        f = open(os.path.join(self.directory, 'pocket.pkl'), mode='wb')
        f.write(pickled)
        f.close()

    # noinspection PyUnresolvedReferences
    def trace_(self, trace: pymc3.backends.base.MultiTrace):
        """
        Reloading requires the model context, excellent.

        :param trace:
        """

        pymc3.backends.ndarray.save_trace(
            trace=trace, directory=os.path.join('trace'), overwrite=True)

        tracefiles = []
        for base, directories, files in os.walk(os.path.join('trace')):
            for file in files:
                tracefiles.append(os.path.join(base, file))

        with zipfile.ZipFile(file=os.path.join(self.directory, 'trace.zip'), mode='w',
                             compression=zipfile.ZIP_DEFLATED, allowZip64=False, compresslevel=6) as tr:
            for tracefile in tracefiles:
                tr.write(tracefile)
