Title: Converting directory of ipynb to pdfs
Date: 2020-02-02
Tags: Accessibility, Teaching

![Image Showing Icons for converting from Jupyter to PDF files](//colbrydi.github.io/images/Jupyter2PDF.png)

I wanted to share the content for one of my courses with some other instructors but it turns out not everyone uses Jupyter notebooks.  

**Option 1:** I decided to convert all of the notebooks to pdfs using [nbconvert](https://nbconvert.readthedocs.io/en/latest/).  However, ```nbconvert``` isn't working on my MacBook.  I think I have too many versions of latex and python installed and I can't quickly find the right magic to get the pdf converter working.  

**Option 2:** However, ```nbconvert``` works great if I convert to html.  So then I had a thought to first convert to html and then print to pdf.  However this option requires me to open and save each html file individually.

**Option 3:** I discovered there are a bunch of tools that convert html to pdf.  Most of them require similar installation I was having trouble with in Option 1. However, Chrome allows me to run in "Headless" mode which may make it easy to automate.


My final solution has the following steps.  Note, this only works on MacOS but conceptually could be converted to work on any system:

1. Use ```nbconvert``` to convert each ipynb in the current directory to html.
2. Use ```Chrome``` headless mode to convert html files to pdfs.
3. Use the ```join``` command to combine all of the pdfs into one file.

Here is a bash script that seems to work:

```bash
#!/bin/bash

mkdir -p HTML

jupyter nbconvert --to html --no-prompt --allow-errors --output-dir HTML *.ipynb

mkdir -p PDF

for file in ./html/*.html
do
	filename=$(basename -- "$file")
	extension="${filename##*.}"
	filename="${filename%.*}"
	/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --headless \
            --virtual-time-budget=10000 \
            --crash-dumps-dir=./html/ \
            --disable-gpu \
            --print-to-pdf=./PDF/${filename}.pdf \
	          --no-margins \
            file://$PWD/$file
done

"/System/Library/Automator/Combine PDF Pages.action/Contents/Resources/join.py" -o CMSE314.pdf ./PDF/*.pdf

open CMSE314.pdf
```

Once I got the bash script working I decided a Makefile would be better

```Makefile
IPYNB_FILES = $(wildcard *.ipynb)
PDF_FILES = $(patsubst %.ipynb, PDF/%.pdf, $(IPYNB_FILES))

all: CMSE314.pdf
        open CMSE314.pdf

HTML/%.html: %.ipynb
        @mkdir -p "$(@D)"
        jupyter nbconvert --to html --no-prompt --allow-errors --output-dir HTML "$<"

PDF/%.pdf: HTML/%.html
        @mkdir -p "$(@D)"
        /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --headless --crash-dumps-dir=$(@D) --disable-gpu --print-to-pdf file://$(PWD)/$<
        mv output.pdf $@

CMSE314.pdf: $(PDF_FILES)
        "/System/Library/Automator/Combine PDF Pages.action/Contents/Resources/join.py" -o CMSE314.pdf $(PDF_FILES)

clean:
        rm -rf HTML
        rm -rf PDF
```

Both seem to work and get the job done. The output for the script is a little easier to read but the makefile is nice because it can be restarted (although It can't be run with the -j parallel option because of the output.pdf temporary file).

Anyway, let me know if you find this helpful. I am sure there are better ways but I needed something quick.
