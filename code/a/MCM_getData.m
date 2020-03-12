%MCM microwave
clc,clear;
fileName = 'pacifier.xlsx';
sheet_name = 'pacifier';

[num, txt, raw] = xlsread(fileName, sheet_name);

star_rate = num(1: size(num,1), 7);
helpful_rate = num(1: size(num,1), 8);
total_vote = num(1: size(num,1), 9);

vine = txt(2: size(num,1), 11);
verifiled = txt(2: size(num,1), 12);

time = txt(2:size(num,1), 15);
time = [time;'4 27 2003'];    % 时间这里经常有漏掉的，手动补充

year = [];
month = [];
day = [];
for i=1:size(time,1)
    change = strsplit(time{i});
    if(size(change,2) < 3)
        change = old_change;    % 插值
    end
    day = [day,str2num(change{2})];
    month = [month,str2num(change{1})];
    year = [year,str2num(change{3})];
    if size(change,2) == 3
        old_change = change;
    end
end

day = day.';
month = month.';
year = year.';

sales = zeros(numel(unique(year)),12);
year_guide = unique(year);
for i=1:size(year,1)
    index = find( year_guide==year(i));
    sales(index,month(i)) = sales(index,month(i)) + 1;
end

tendcy = zeros(size(sales,1),size(sales,2));
for i = 1:size(sales,1)
    tendcy(i,:) = sales(i,:) ./ sum(sales(i,:)); 
end
fix = [];
for i = 1:size(tendcy,1)
     fix = [fix,tendcy(i,:)];
end
tendcy = fix.';
xlswrite('paci_tend.xlsx',tendcy);

star_rate = star_rate./5;
year_guide = unique(year);
Nnum = zeros(numel(unique(year)),12);
pre_star = zeros(numel(unique(year)),12);
for i = 1:size(star_rate,1)
     index = find( year_guide==year(i));
     Nnum(index,month(i)) = Nnum(index,month(i)) + 1;
     pre_star(index,month(i)) = pre_star(index,month(i)) + star_rate(i);
end

for i=1:size(Nnum,1)
    for j=1:size(Nnum,2)
        if Nnum(i,j) == 0
            ;
        else
            pre_star(i,j) = pre_star(i,j) / Nnum(i,j); 
        end
         
    end
end

star_line = [];
for i=1:size(pre_star,1)
    star_line = [star_line,pre_star(i,:)]; 
end

star_line = star_line.';

xlswrite('paci_star.xlsx',star_line);

[num, txt, raw] = xlsread('pacifier_txt.xlsx', 'pacifier');

title = txt(1: size(num,1), 1);
body = txt(1: size(num,1), 2);

num1 = num(1: size(num,1), 1);
num2 = num(1: size(num,1), 2);
num3 = num(1: size(num,1), 3);
num4 = num(1: size(num,1), 4);

w_sub = 1/(1+exp(1-1));    %主观的权值
w_obj = 1/(1+exp(0-1));    %客观的权值

pos_gra = [];
neg_gra = [];
pos_txt = cell(0);
neg_txt = cell(0);
mid_txt = cell(0);

Grade = [];

for i = 1:size(body)
    i
    if num2(i) > 0
        if num4(i) > 0
            grad = (w_sub * num2(i) + 1)/2;
            Grade = [Grade;grad];
        else
            grad = (w_obj * num2(i) + 1)/2;
            Grade = [Grade;grad];
        end
    elseif num2(i) < 0 
        if num4(i) > 0
            grad = ((w_sub * num2(i))+1)/2;
            Grade = [Grade;grad];
        else
            grad = ((w_obj * num2(i))+1)/2;
            Grade = [Grade;grad];
        end
    else
        grad = 0.5;
        Grade = [Grade;grad];
    end
end

year_guide = unique(year);
Nnum = zeros(numel(unique(year)),12);
pre_txt = zeros(numel(unique(year)),12);
for i = 1:size(Grade,1)
     index = find( year_guide==year(i));
     Nnum(index,month(i)) = Nnum(index,month(i)) + 1;
     pre_txt(index,month(i)) = pre_txt(index,month(i)) + Grade(i);
end

for i=1:size(Nnum,1)
    for j=1:size(Nnum,2)
        if Nnum(i,j) == 0
            ;
        else
            pre_txt(i,j) = pre_txt(i,j) / Nnum(i,j); 
        end
         
    end
end

txt_line = [];
for i=1:size(pre_txt,1)
    txt_line = [txt_line,pre_txt(i,:)]; 
end

txt_line = txt_line.';
xlswrite('paci_txt.xlsx',star_line);



























