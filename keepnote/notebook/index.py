
import os

from sqlite3 import dbapi2 as sqlite

import keepnote



INDEX_FILE = "index.sqlite"



def get_index_file(notebook):
    return os.path.join(notebook.get_pref_dir(), INDEX_FILE)



class NoteBookIndex (object):
    """Index for a NoteBook"""

    def __init__(self, notebook):
        self._notebook = notebook

        self.init_index()


    def init_index(self):
        
        index_file = get_index_file(self._notebook)
        if not os.path.exists(index_file):
            # create index
            con = sqlite.connect(index_file) #, isolation_level="DEFERRED")
            cur = con.cursor()

            # init NodeGraph table
            query = """CREATE TABLE IF NOT EXISTS NodeGraph 
                       (nodeid TEXT,
                        parentid TEXT,
                        basename TEXT);
                    """
            cur.execute(query)
            con.commit()

            
            con.close()


    