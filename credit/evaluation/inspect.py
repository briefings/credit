import json
import hmac
import hashlib
import pickle


class Inspect:

    def __init__(self, path_of_kappa: str, path_of_pickle: str):
        """
        
        :param path_of_kappa: The path to the kappa file (JSON)
        :param path_of_pickle: The path to the pickled model+
        """

        self.path_of_kappa = path_of_kappa
        self.path_of_pickle = path_of_pickle

    def key(self) -> bytes:
        """

        :return:
        """

        f = open(self.path_of_kappa)
        kappa = json.load(f)
        f.close()

        return bytes.fromhex(kappa['kappa'])

    def read(self):
        """

        :return:
        """

        with open(self.path_of_pickle, 'rb') as f:
            digest = f.readline()
            pickled = f.read()

        digest = digest.rstrip(b'\n')

        return digest, pickled

    def exc(self):
        """
        
        :return:
        """

        key = self.key()
        digest, pickled = self.read()

        recomputed = hmac.digest(key, pickled, digest=hashlib.sha384)

        if not hmac.compare_digest(digest, recomputed):
            raise Exception('unverifiable byte stream')
        else:
            return pickle.loads(pickled)            
