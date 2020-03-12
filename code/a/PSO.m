%PSO
close all;
clc;

txt_grade = xlsread('paci_txt.xlsx', 'Sheet1');
star_grade = xlsread('paci_star.xlsx', 'Sheet1');
tend_grade = xlsread('paci_tend.xlsx', 'Sheet1');
tend_grade(1) = [];
txt_grade(size(txt_grade,1)) = [];
star_grade(size(star_grade,1)) = [];

N = 1000;%种群规模
D = 2;%粒子维度
T = 100;%迭代次数
Xmax = 1;
Xmin = 0;
C1 = 0.5; %学习因子1
C2 = 0.5; %学习因子2
w = 0.8; %惯性权重
Vmax = 1; % 最大飞行速度
Vmin = -1;% 最小飞行速度
popx = rand(N,D)*(Xmax-Xmin)+Xmin;% 初试化粒子群的位置(粒子位置是个D维向量)
popv = rand(N,D)*(Vmax-Vmin)+Vmin;%初始化粒子群的速度（粒子速度是个D维向量）
%初始化每个历史最优粒子
pBest = popx;
pBestValue = [];
for i=1:N
     pBestValue = [pBestValue;func_fitness(pBest(i,:),txt_grade,star_grade,tend_grade)];
end
%pBestValue = func_fitness(pBest,txt_grade,star_grade,tend_grade);
%初始化全局历史最优粒子
[gBestValue,index] = min(func_fitness(popx,txt_grade,star_grade,tend_grade));
gBest = popx(index,:);
for t=1:T
    for i=1:N
        t
        i
        %更新个体的位置和速度
        popv(i,:) = w*popv(i,:)+C1*rand*(pBest(i,:)-popx(i,:))+C2*rand*(gBest-popx(i,:));
        popx(i,:) = popx(i,:)+popv(i,:);
        %边界处理，超过定义域范围就取该范围极值
        index = popv(i,:)>Vmax | popv(i,:)<Vmin ;
        popv(i,index) = rand*(Vmax-Vmin)+Vmin ;
        index = find(popx(i,:)>Xmax | popx(i,:)<Xmin);
        popx(i,index) = rand*(Xmax-Xmin) + Xmin;
        %更新粒子历史最优
        if func_fitness(popx(i,:),txt_grade,star_grade,tend_grade) < pBestValue(i)
            pBest(i,:) = popx(i,:);
            pBestValue(i) = func_fitness(popx(i,:),txt_grade,star_grade,tend_grade);
        elseif pBestValue(i) < gBestValue
            gBest = pBest(i,:);
            gBestValue = pBestValue(i);
        end
    end
      %每代最优解对应的目标函数值
      tBest(t) = func_fitness(gBest,txt_grade,star_grade,tend_grade);%目标函数
end
figure
plot(tBest);
xlabel('迭代次数');
ylabel('适应度值');
%title('适应度·进化曲线');