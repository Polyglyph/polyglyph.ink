#!/bin/bash

cd typeface
poetry run python process.py
cd ..

echo "Moving generated typefaces into public"

mkdir -p public/glyphs
cp typeface/output_flat/* public/glyphs/

echo "Making compiled zip file of glyphs"
mkdir -p public/temp/typeface_builder/polyglyph
mkdir -p public/temp/typeface_builder/polyglyph_flat

cp -r typeface/output/* public/temp/typeface_builder/polyglyph
cp typeface/output_flat/* public/temp/typeface_builder/polyglyph_flat

rm public/polyglyph.zip
cd public/temp/typeface_builder

zip -qr ../../polyglyph.zip polyglyph polyglyph_flat
cd ../../..

rm -r public/temp