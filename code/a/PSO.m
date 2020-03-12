%PSO
close all;
clc;

txt_grade = xlsread('paci_txt.xlsx', 'Sheet1');
star_grade = xlsread('paci_star.xlsx', 'Sheet1');
tend_grade = xlsread('paci_tend.xlsx', 'Sheet1');
tend_grade(1) = [];
txt_grade(size(txt_grade,1)) = [];
star_grade(size(star_grade,1)) = [];

N = 1000;%��Ⱥ��ģ
D = 2;%����ά��
T = 100;%��������
Xmax = 1;
Xmin = 0;
C1 = 0.5; %ѧϰ����1
C2 = 0.5; %ѧϰ����2
w = 0.8; %����Ȩ��
Vmax = 1; % �������ٶ�
Vmin = -1;% ��С�����ٶ�
popx = rand(N,D)*(Xmax-Xmin)+Xmin;% ���Ի�����Ⱥ��λ��(����λ���Ǹ�Dά����)
popv = rand(N,D)*(Vmax-Vmin)+Vmin;%��ʼ������Ⱥ���ٶȣ������ٶ��Ǹ�Dά������
%��ʼ��ÿ����ʷ��������
pBest = popx;
pBestValue = [];
for i=1:N
     pBestValue = [pBestValue;func_fitness(pBest(i,:),txt_grade,star_grade,tend_grade)];
end
%pBestValue = func_fitness(pBest,txt_grade,star_grade,tend_grade);
%��ʼ��ȫ����ʷ��������
[gBestValue,index] = min(func_fitness(popx,txt_grade,star_grade,tend_grade));
gBest = popx(index,:);
for t=1:T
    for i=1:N
        t
        i
        %���¸����λ�ú��ٶ�
        popv(i,:) = w*popv(i,:)+C1*rand*(pBest(i,:)-popx(i,:))+C2*rand*(gBest-popx(i,:));
        popx(i,:) = popx(i,:)+popv(i,:);
        %�߽紦������������Χ��ȡ�÷�Χ��ֵ
        index = popv(i,:)>Vmax | popv(i,:)<Vmin ;
        popv(i,index) = rand*(Vmax-Vmin)+Vmin ;
        index = find(popx(i,:)>Xmax | popx(i,:)<Xmin);
        popx(i,index) = rand*(Xmax-Xmin) + Xmin;
        %����������ʷ����
        if func_fitness(popx(i,:),txt_grade,star_grade,tend_grade) < pBestValue(i)
            pBest(i,:) = popx(i,:);
            pBestValue(i) = func_fitness(popx(i,:),txt_grade,star_grade,tend_grade);
        elseif pBestValue(i) < gBestValue
            gBest = pBest(i,:);
            gBestValue = pBestValue(i);
        end
    end
      %ÿ�����Ž��Ӧ��Ŀ�꺯��ֵ
      tBest(t) = func_fitness(gBest,txt_grade,star_grade,tend_grade);%Ŀ�꺯��
end
figure
plot(tBest);
xlabel('��������');
ylabel('��Ӧ��ֵ');
%title('��Ӧ�ȡ���������');