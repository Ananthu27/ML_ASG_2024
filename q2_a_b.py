from q1 import gen_normal_2d
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__' : 
    
    ## q2 a 
    mean1 = 5
    var1 = 1
    mean2 = 30
    var2 =20
    data = gen_normal_2d(mean1=mean1, mean2=mean2, var1=var1, var2=var2, size=800)
    train_data, test_data = train_test_split(data,test_size=.2)

    ## q2 b 
    # formula used : 
    #     ♦ b₁ = (nΣxᵢyᵢ-ΣxᵢΣyᵢ)/(nΣxᵢ²-(Σxᵢ)²) 
	#     ♦ b₀ = (Σyᵢ-b₁Σxᵢ)/n
 
    df_train = pd.DataFrame(train_data,columns=['x','y'])
    
    n = len(df_train)
    sum_x = sum(df_train['x'])
    sum_y = sum(df_train['y'])
    sum_xy = sum(df_train['x']*df_train['y'])
    sum_x2 = sum(df_train['x']*df_train['x'])
    b1 = (n*sum_xy-sum_x*sum_y)/(n*sum_x2-sum_x**2)
    b0 = (sum_y-b1*sum_x)/n
    
    df_train['predicted'] = b0+b1*df_train['x']
    
    plt.figure(figsize=(12, 8))
    plt.scatter(df_train['x'],df_train['y'],s=2)
    plt.title("Linear Regression")
    plt.xlabel("Distribution of DIM1 (μ=%d,σ=%d)"%(mean1,var1))
    plt.ylabel("Distribution of DIM2 (μ=%d,σ=%d)"%(mean2,var2))

    train_error = sum((df_train['y']-df_train['predicted'])**2)/n
    df_test = pd.DataFrame(test_data,columns=['x','y'])
    df_test['predicted'] = b0+b1*df_test['x']
    test_error = sum((df_test['y']-df_test['predicted'])**2)/len(df_test)
    plt.plot(
        df_train['x'],df_train['predicted'],color='red',lw=1,
        label='y=%.2f+%.2fx, Train MSE =%.2f, Test MSE=%.2f'%(b0,b1,train_error,test_error)
    )
    plt.legend(loc="lower right")
    plt.show()