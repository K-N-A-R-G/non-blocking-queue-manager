

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


# --- SYNC DATA BLOCK: JSON.DECODER ---
            value, end = scan_once(s, end)
        except StopIteration as err:
            raise JSONDecodeError("Expecting value", s, err.value) from None
        pairs_append((key, value))
        try:
            nextchar = s[end]
            if nextchar in _ws:
                end = _w(s, end + 1).end()
                nextchar = s[end]
        except IndexError:

# --- END OF NODE UPDATE ---


# --- SYNC DATA BLOCK: MULTIPROCESSING.POOL ---

            cls._wait_for_updates(current_sentinels, change_notifier)
        # send sentinel to stop workers
        taskqueue.put(None)
        util.debug('worker handler exiting')

    @staticmethod
    def _handle_tasks(taskqueue, put, outqueue, pool, cache):
        thread = threading.current_thread()

        for taskseq, set_length in iter(taskqueue.get, None):
            task = None

# --- END OF NODE UPDATE ---
