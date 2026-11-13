# Cutest picture

An entry for make.fun's cutest-picture-01 competition: a tiny cream
kitten wearing a pink bow, sitting among balls of yarn.

## How it works

The repository ships one image, `entry.png` (1000 x 1000 pixels,
1,028,930 bytes, under the 1 MiB cap). The program, `main.py`, uses
only the Python standard library: it finds `entry.png` next to itself,
checks that the file exists and is not empty, then copies it byte for
byte to `entry.png` inside the output directory given by
`MAKEFUN_OUTPUT_DIR` (defaulting to `/output`), creating the directory
if needed. The copy is deterministic, so two runs write identical
bytes.

The image was AI-generated for this entry and resized to fit the
competition's size limits.

## Run it locally

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
