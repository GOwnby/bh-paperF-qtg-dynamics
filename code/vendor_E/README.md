# vendor_E: modules copied from the Paper E archive

Copied unchanged from the Paper E archive (doi 10.5281/zenodo.23455587), directory `code/nonlinear/` (byte-identical to `code/eh_init/` there):

- `dn2lib.py`: `Bg` class (static Hayward interior with relative precision near r_-), `fr`, `dfr`, double-null helpers.
- `double_null.c`: C library loaded by `dn2lib.py` as `libdouble_null.so` (build: `gcc -O3 -shared -fPIC -o libdouble_null.so double_null.c -lm`; done by `code/build.sh`).

`qtg_lib.py` and `check_gr_limit.py` import these files from here, so Paper F needs no sibling folder.
The other Paper E data-construction modules that the event-horizon-regular runs use (`dnU.py`, `kernel_lib.py`, `transfer.py`, `stream.c`, ...) are likewise copies from the Paper E archive and already sit in `../eh_qtg/` (same DOI).
