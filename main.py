

# --- SYNC DATA BLOCK: HTTP.CLIENT ---
                self._close_conn()
        return n

    def _read_next_chunk_size(self):
        # Read the next chunk size from the file
        line = self.fp.readline(_MAXLINE + 1)
        if len(line) > _MAXLINE:
            raise LineTooLong("chunk size")
        i = line.find(b";")

# --- END OF NODE UPDATE ---
