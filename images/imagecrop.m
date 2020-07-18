function im2 = imagecrop(imname)
% Written by Dirk Colbry 
% 01-27-2014
% Tool to select and crop an image
 
im = imread(imname); done=false;

while(~done)
	image(im); axis off; axis equal;
	title('Select upper right corner of cropped area')
	[x1,y1] = ginput(1);

	title('Select lower right corner of cropped area')
	[x2,y2] = ginput(1);
	im2 = im(y1:y2, x1:x2, :);
	image(im2); axis off; axis equal;

	in = input('Is this correct (Yes/No)', 's')
	if (strcmp(in,'Yes'))
		done = true;
	end
end


