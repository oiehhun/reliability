def ra1(data, t):
    'reliability analysis1\
    data : 데이터 , t : 단위시간'  #함수설명
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    m = data.mean()
    l = 1/m
    M = np.round(data.mean(), 3)  #평균수명
    L = np.round(1/m, 3)  #고장률
    R = np.round(np.exp(-l*t), 3)  #고장날 확률
    plt.hist(data)  #히스토그램
    print('평균수명 \n:', M)
    print('고장률 \n:', L)
    print('단위시간 t 동안 고장나지 않을 확률 \n:', R)
    plt.show()

def ra2(r, Cr, Ci):
    'reliability analysis 2\
    r : 단위시간당 시스템의 평균고장횟수 , Cr : 고장수리비용 , Ci : 점검비용'  
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import warnings
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    n_star = np.round(np.sqrt(r*Cr/Ci), 0)  #최적의 점검횟수 근사값
    n_s = np.round(n_star + 10, 0)
    i = np.arange(0, n_s+10)
    Cn = np.round((r/i)*Cr+i*Ci, 3)  #총 기대비용
    CN = pd.Series(Cn)
    col_name = ['기대비용']
    CN_df = pd.DataFrame(CN, columns = col_name)
    CNm = CN_df.min()
    index = [np.where(i == CN_df)[0].tolist()[0]for i in CNm] #최적 점검횟수
    x = np.array(index)
    plt.plot(i, Cn)  #그래프 그리기
    plt.xlabel('The number of inspections')  #라벨
    plt.ylabel('Expected cost')
    plt.annotate('optimal number', xy=(x,CNm), xytext=(x+5,CNm+500), arrowprops={'color':'green'})  #주석
    plt.show()
    print('최적 점검횟수 :' , index)  #인덱스 추출
    print('총 기대비용 :', CN_df['기대비용'].min())
