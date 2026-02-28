# INSTALLATION instructions
Follow these directions to create your own website or blog using github pages and the software called pelican, which allows processes markdown and jupyter notebook files into HTML for you. Very easy to update content on your website without dealing with HTML syntax.

### 1) Ensure that both python and pelican are installed on your computer
~~~~
pip install pelican markdown
~~~~
### 2) Create your own blog folder on your computer
You can name it whatever you want - all files related to your blog should be inside of this folder. When you run a pelican command later on in these instructions, it should be run in this folder using the terminal.

### 3) Download this repository into your blog folder
Using either git pull or downloading the zip file

### 4) Open yourblog/output/index.html
Open this file using a web browser. This allows you to see the default webpage I've set, with an MSU theme

### 5) Make changes to files within yourblog/content
This allows you to customize your website

Files in the 'Pages' folder can be set to automatically be displayed in the menu bar - they do not have multiple posts, just one static page. Usually for content that won't change, such as contact info.

Categories help group files of the same subject. Categories can be by grouping files in the same folder or by setting the category within the file. Categories can also be customized to be on the menu bar. This helps you organize your posts, and separate static pages with blogs.

More tips can be found [here](http://docs.getpelican.com/en/3.6.3/tips.html).

### 6) Test changes
Do this by running the following code in your Terminal, located in your blog folder
~~~~
pelican content
~~~~
This runs the pelican software on everything inside yourblog/content folder, converting markdown files into html. This makes updating your pages much quicker and easier than rewriting HTML code.

Ever time you run 'pelican content,' the your blog's output folder will be updated. So even if you delete the folder, you can always regenerate it by running that command. That is the power or pelican!

Open your index.html in the output folder to see the new changes

### 7) Upload to your github.io site
Follow the directions on creating your own github.io site at Github Pages, which should be very quick and easy. Once you commit everything in your blog's output folder to your new GitHub repository (which can be done with the a git push or simply by dragging the files), your new website should be up and running online within the minute!
