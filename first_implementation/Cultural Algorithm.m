clc;
clear;
close all;

%% Problem Definition

CostFunction=@(x) Sphere(x);        % Cost Function

nVar=5;             % Number of Decision Variables (Unknown variables)

VarSize=[1 nVar];   % Decision Variables Matrix Size

VarMin=-10;         % Decision Variables Lower Bound
VarMax= 10;         % Decision Variables Upper Bound

%% Cultural Algorithm Settings

MaxIt=500;          % Maximum Number of Iterations

nPop=50;            % Population Size

pAccept=0.35;                   % Acceptance Ratio
nAccept=round(pAccept*nPop);    % Number of Accepted Individuals

%Dynamic method for riching nAccept
% for i=1 : it   
%     nAccept= round(nPop*gamma/it);
%     
% end

alpha=0.25;

beta=0.5;

%% Initialization

% Initialize Culture
Culture.Situational.Cost=inf;
Culture.Normative.Min=inf(VarSize);
Culture.Normative.Max=-inf(VarSize);
Culture.Normative.L=inf(VarSize);
Culture.Normative.U=inf(VarSize);

% Empty Individual Structure
empty_individual.Position=[];
empty_individual.Cost=[];

% Initialize Population Array
pop=repmat(empty_individual,nPop,1);

% Generate Initial Solutions
for i=1:nPop
    pop(i).Position=unifrnd(VarMin,VarMax,VarSize);
    pop(i).Cost=CostFunction(pop(i).Position);
end

% Sort Population
[~, SortOrder]=sort([pop.Cost]);
pop=pop(SortOrder);

% Adjust Culture
spop=pop(1:nAccept);
Culture=AdjustCulture(Culture,spop);

% Update Best Solution Ever Found
BestSol=Culture.Situational;

% Array to Hold Best Costs
BestCost=zeros(MaxIt,1);

%% Cultural Algorithm Main Loop

for it=1:MaxIt
    
    % Influnce of Culture
    for i=1:nPop
        
        % % 1st Method, using only the normative component
%         sigma=alpha*Culture.Normative.Size;
%         pop(i).Position=pop(i).Position+sigma.*randn(VarSize);
        
        % 2nd Method, using only the situational component
%         for j=1:nVar
%            sigma=0.1*(VarMax-VarMin);
%            dx=sigma*randn;
%            if pop(i).Position(j)<Culture.Situational.Position(j)
%                dx=abs(dx);
%            elseif pop(i).Position(j)>Culture.Situational.Position(j)
%                dx=-abs(dx);
%            end
%            pop(i).Position(j)=pop(i).Position(j)+dx;
%         end
        
        % 3rd Method
        for j=1:nVar
          sigma=alpha*Culture.Normative.Size(j);
          dx=sigma*randn;
          if pop(i).Position(j)<Culture.Situational.Position(j)
              dx=abs(dx);
          elseif pop(i).Position(j)>Culture.Situational.Position(j)
              dx=-abs(dx);
          end
          pop(i).Position(j)=pop(i).Position(j)+dx;
        end        
        
        % 4th Method
%         for j=1:nVar
%           sigma=alpha*Culture.Normative.Size(j);
%           dx=sigma*randn;
%           if pop(i).Position(j)<Culture.Normative.Min(j)
%               dx=abs(dx);
%           elseif pop(i).Position(j)>Culture.Normative.Max(j)
%               dx=-abs(dx);
%           else
%               dx=beta*dx;
%           end
%           pop(i).Position(j)=pop(i).Position(j)+dx;
%         end        
        
        pop(i).Cost=CostFunction(pop(i).Position);
    end
    
    % Sort Population
    [~, SortOrder]=sort([pop.Cost]);
    pop=pop(SortOrder);

    % Adjust Culture
    spop=pop(1:nAccept);
    Culture=AdjustCulture(Culture,spop);

    % Update Best Solution Ever Found
    BestSol=Culture.Situational;
    
    % Store Best Cost Ever Found
    BestCost(it)=BestSol.Cost;
    
    % Show Iteration Information
    disp(['Iteration ' num2str(it) ': Best Cost = ' num2str(BestCost(it))]);
    
end

%% Results

figure;
%plot(BestCost,'LineWidth',2);
semilogy(BestCost,'LineWidth',2);
xlabel('Iteration');
ylabel('Best Cost');

