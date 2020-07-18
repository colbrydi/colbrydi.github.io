function im = moviestitch(im1, im2, t)
% Example:
%    i = imread('westconcordaerial.png');
%    im = moviestitch(i,i,[100 200]);
%    imshow(im);
t = int32(round(t));
xb = [1 1+t(1) size(im1,1) size(im2,1)+t(1)];
yb = [1 1+t(2) size(im1,2) size(im2,2)+t(2)];

xmin=min(xb);
xmax=max(xb);
ymin=min(yb);
ymax=max(yb);

im=uint8(zeros(xmax-xmin, ymax-ymin, 3));

r1 = 1;
r2 = t(1);
c1 = 1;
c2 = t(2);
bound=[r2 size(im2,1) c2 size(im2,2)];

if(1+t(1) < 1)
    r1=-t(1);
    r2=1;
    bound(1)=r1;
    bound(2)=size(im2,1);
    disp('swapping r');
end

if(1+t(2) < 1)
    c1=-t(2);
    c2=1;
    bound(3)=c1;
    bound(4)=size(im2,2);
    disp('swapping c');
end

%bound is the coordinates of the overlap region in the new image
[a b] = meshgrid( 1:bound(4)-bound(3)+1, 1:bound(2)-bound(1)+1);

%Swap the directions if negative overlap
if(1+t(1) < 1)
    b = max(max(b))-b;
end
if(1+t(2) < 1)
    a = max(max(a))-a;
end

%m1 minimum distance to upper left edges
m1 = min(a,b);

%m2 minimum distance to lower right edges
m2 = min(max(max(a))-a, max(max(b))-b);

%tot total minimum distance between two edges
tot = m1 + m2;

% Ratio of pixels taken from each image.
WA(:,:,1) = double(m1) ./ double(tot);
WA(:,:,2) = double(m1) ./ double(tot);
WA(:,:,3) = double(m1) ./ double(tot);
WB(:,:,1) = double(m2) ./ double(tot);
WB(:,:,2) = double(m2) ./ double(tot);
WB(:,:,3) = double(m2) ./ double(tot);

% IA is the overlap section in image WA
im(r1:r1+size(im1,1)-1,c1:c1+size(im1,2)-1,:) = im1;  
IA=im(bound(1):bound(2),bound(3):bound(4),:);
im(bound(1):bound(2),bound(3):bound(4),:) = 0;

% IB is the overlap section in image WB
im(r2:r2+size(im2,1)-1,c2:c2+size(im2,2)-1,:) = im2;        
IB=im(bound(1):bound(2),bound(3):bound(4),:);

im(bound(1):bound(2),bound(3):bound(4),:) = uint8(double(IA).*WB + double(IB).*WA);



    
   
