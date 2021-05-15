#!/bin/bash

cd typeface
poetry run python process.py
cd ..

echo "Moving generated typefaces into public"

mkdir -p public/glyphs
cp typeface/output_flat/* public/glyphs/