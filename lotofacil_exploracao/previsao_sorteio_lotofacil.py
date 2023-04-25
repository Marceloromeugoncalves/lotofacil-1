import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense

# Carrega o arquivo xlsx com os dados de entrada
df = pd.read_excel('./dados/historico_lotofacil.xlsx', sheet_name='Sorteios')

# Realiza a separação das bolas sorteadas em uma lista de listas
resultado = df['Resultado'].str.split(';').apply(lambda x: [int(num) for num in x])

# Cria uma matriz de entrada para a rede neural
X = np.array(resultado.tolist())

# Cria um vetor de saída para a rede neural
y = np.array(df['Resultado'].apply(lambda x: int(x.split(';')[0])).tolist())

# Redimensionar os dados de entrada para ter 15 características
X = X[:, :15]

# Criar o modelo de rede neural
model = Sequential()
model.add(Dense(64, input_dim=15, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='linear'))

# Compilar o modelo
model.compile(loss='mean_squared_error', optimizer='adam')

# Treinar o modelo
model.fit(X, y, epochs=100, batch_size=32)

# Realizar a predição do próximo resultado
proximo_sorteio = np.array([[18, 20, 25, 23, 10, 11, 24, 14, 6, 2, 13, 9, 5, 16]])
predicao = model.predict(proximo_sorteio)
print("Predição do próximo resultado:", predicao)

"""
Epoch 1/100
88/88 [==============================] - 1s 3ms/step - loss: 79.4268
Epoch 2/100
88/88 [==============================] - 0s 2ms/step - loss: 5.1198
Epoch 3/100
88/88 [==============================] - 0s 3ms/step - loss: 0.8709
Epoch 4/100
88/88 [==============================] - 0s 2ms/step - loss: 0.5931
Epoch 5/100
88/88 [==============================] - 0s 3ms/step - loss: 0.4542
Epoch 6/100
88/88 [==============================] - 0s 2ms/step - loss: 0.3452
Epoch 7/100
88/88 [==============================] - 0s 2ms/step - loss: 0.2844
Epoch 8/100
88/88 [==============================] - 0s 2ms/step - loss: 0.2236
Epoch 9/100
88/88 [==============================] - 0s 2ms/step - loss: 0.2017
Epoch 10/100
88/88 [==============================] - 0s 3ms/step - loss: 0.1542
Epoch 11/100
88/88 [==============================] - 0s 2ms/step - loss: 0.1221
Epoch 12/100
88/88 [==============================] - 0s 2ms/step - loss: 0.1029
Epoch 13/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0933
Epoch 14/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0779
Epoch 15/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0657
Epoch 16/100
88/88 [==============================] - 0s 4ms/step - loss: 0.0521
Epoch 17/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0442
Epoch 18/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0394
Epoch 19/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0343
Epoch 20/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0304
Epoch 21/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0236
Epoch 22/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0222
Epoch 23/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0177
Epoch 24/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0147
Epoch 25/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0148
Epoch 26/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0129
Epoch 27/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0100
Epoch 28/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0097
Epoch 29/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0084
Epoch 30/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0064
Epoch 31/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0060
Epoch 32/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0057
Epoch 33/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0047
Epoch 34/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0077
Epoch 35/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0037
Epoch 36/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0050
Epoch 37/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0041
Epoch 38/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0046
Epoch 39/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0051
Epoch 40/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0032
Epoch 41/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0046
Epoch 42/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0035
Epoch 43/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0031
Epoch 44/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0029
Epoch 45/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0028
Epoch 46/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0033
Epoch 47/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0055
Epoch 48/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0025
Epoch 49/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0032
Epoch 50/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0085
Epoch 51/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0030
Epoch 52/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0109
Epoch 53/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0029
Epoch 54/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0051
Epoch 55/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0024
Epoch 56/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0023
Epoch 57/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0067
Epoch 58/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0058
Epoch 59/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0110
Epoch 60/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0073
Epoch 61/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0062
Epoch 62/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0086
Epoch 63/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0025
Epoch 64/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0025
Epoch 65/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0028
Epoch 66/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0076
Epoch 67/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0093
Epoch 68/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0088
Epoch 69/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0021
Epoch 70/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0052
Epoch 71/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0031
Epoch 72/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0026
Epoch 73/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0064
Epoch 74/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0109
Epoch 75/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0051
Epoch 76/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0042
Epoch 77/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0138
Epoch 78/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0061
Epoch 79/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0029
Epoch 80/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0053
Epoch 81/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0030
Epoch 82/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0028
Epoch 83/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0047
Epoch 84/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0026
Epoch 85/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0115
Epoch 86/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0058
Epoch 87/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0030
Epoch 88/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0037
Epoch 89/100
88/88 [==============================] - 0s 4ms/step - loss: 0.0025
Epoch 90/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0041
Epoch 91/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0085
Epoch 92/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0042
Epoch 93/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0072
Epoch 94/100
88/88 [==============================] - 0s 4ms/step - loss: 0.0070
Epoch 95/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0265
Epoch 96/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0012
Epoch 97/100
88/88 [==============================] - 0s 2ms/step - loss: 8.1148e-04
Epoch 98/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0038
Epoch 99/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0043
(venv) PS C:\Users\ADM\Desktop\Marcelo\Developer\Projetos\lotofacil\lotofacil_exploracao> python previsao_sorteio_lotofacil.py
Epoch 1/100
88/88 [==============================] - 1s 3ms/step - loss: 19.0819
Epoch 2/100
88/88 [==============================] - 0s 4ms/step - loss: 1.2970
Epoch 3/100
88/88 [==============================] - 0s 3ms/step - loss: 0.6702
Epoch 4/100
88/88 [==============================] - 0s 5ms/step - loss: 0.4358
Epoch 5/100
88/88 [==============================] - 0s 2ms/step - loss: 0.2884
Epoch 6/100
88/88 [==============================] - 0s 3ms/step - loss: 0.2094
Epoch 7/100
88/88 [==============================] - 0s 2ms/step - loss: 0.1625
Epoch 8/100
88/88 [==============================] - 0s 3ms/step - loss: 0.1302
Epoch 9/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0891
Epoch 10/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0698
Epoch 11/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0648
Epoch 12/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0548
Epoch 13/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0416
Epoch 14/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0427
Epoch 15/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0292
Epoch 16/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0283
Epoch 17/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0227
Epoch 18/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0208
Epoch 19/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0169
Epoch 20/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0162
Epoch 21/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0182
Epoch 22/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0138
Epoch 23/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0085
Epoch 24/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0100
Epoch 25/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0100
Epoch 26/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0111
Epoch 27/100
88/88 [==============================] - 0s 4ms/step - loss: 0.0163
Epoch 28/100
88/88 [==============================] - 0s 4ms/step - loss: 0.0158
Epoch 29/100
88/88 [==============================] - 0s 4ms/step - loss: 0.0104
Epoch 30/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0114
Epoch 31/100
88/88 [==============================] - 0s 4ms/step - loss: 0.0066
Epoch 32/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0061
Epoch 33/100
88/88 [==============================] - 0s 4ms/step - loss: 0.0062
Epoch 34/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0096
Epoch 35/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0056
Epoch 36/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0114
Epoch 37/100
88/88 [==============================] - 0s 4ms/step - loss: 0.0085
Epoch 38/100
88/88 [==============================] - 0s 4ms/step - loss: 0.0102
Epoch 39/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0059
Epoch 40/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0053
Epoch 41/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0052
Epoch 42/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0086
Epoch 43/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0065
Epoch 44/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0088
Epoch 45/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0064
Epoch 46/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0041
Epoch 47/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0036
Epoch 48/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0069
Epoch 49/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0105
Epoch 50/100
88/88 [==============================] - 0s 5ms/step - loss: 0.0080
Epoch 51/100
88/88 [==============================] - 0s 4ms/step - loss: 0.0039
Epoch 52/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0072
Epoch 53/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0089
Epoch 54/100
88/88 [==============================] - 0s 5ms/step - loss: 0.0226
Epoch 55/100
88/88 [==============================] - 0s 4ms/step - loss: 0.0090
Epoch 56/100
88/88 [==============================] - 0s 5ms/step - loss: 0.0044
Epoch 57/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0117
Epoch 58/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0085
Epoch 59/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0062
Epoch 60/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0013
Epoch 61/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0057
Epoch 62/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0072
Epoch 63/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0091
Epoch 64/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0039
Epoch 65/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0030
Epoch 66/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0077
Epoch 67/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0089
Epoch 68/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0027
Epoch 69/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0095
Epoch 70/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0068
Epoch 71/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0076
Epoch 72/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0057
Epoch 73/100
88/88 [==============================] - 0s 5ms/step - loss: 0.0076
Epoch 74/100
88/88 [==============================] - 0s 4ms/step - loss: 0.0063
Epoch 75/100
88/88 [==============================] - 0s 4ms/step - loss: 0.0137
Epoch 76/100
88/88 [==============================] - 0s 4ms/step - loss: 0.0035
Epoch 77/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0077
Epoch 78/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0114
Epoch 79/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0047
Epoch 80/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0025
Epoch 81/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0059
Epoch 82/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0091
Epoch 83/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0041
Epoch 84/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0031
Epoch 85/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0157
Epoch 86/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0091
Epoch 87/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0027
Epoch 88/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0017
Epoch 89/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0022
Epoch 90/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0079
Epoch 91/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0052
Epoch 92/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0087
Epoch 93/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0202
Epoch 94/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0048
Epoch 95/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0042
Epoch 96/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0067
Epoch 97/100
88/88 [==============================] - 0s 2ms/step - loss: 0.0019
Epoch 98/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0017
Epoch 99/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0035
Epoch 100/100
88/88 [==============================] - 0s 3ms/step - loss: 0.0075
Traceback (most recent call last):
  File "C:\Users\ADM\Desktop\Marcelo\Developer\Projetos\lotofacil\lotofacil_exploracao\previsao_sorteio_lotofacil.py", line 35, in <module>
    predicao = model.predict(proximo_sorteio)
  File "C:\Users\ADM\Desktop\Marcelo\Developer\Projetos\lotofacil\lotofacil_exploracao\venv\lib\site-packages\keras\utils\traceback_utils.py", line 70, in error_handler
    raise e.with_traceback(filtered_tb) from None
  File "C:\Users\ADM\AppData\Local\Temp\__autograph_generated_filef0tku8dd.py", line 15, in tf__predict_function
    retval_ = ag__.converted_call(ag__.ld(step_function), (ag__.ld(self), ag__.ld(iterator)), None, fscope)
ValueError: in user code:

    File "C:\Users\ADM\Desktop\Marcelo\Developer\Projetos\lotofacil\lotofacil_exploracao\venv\lib\site-packages\keras\engine\training.py", line 2169, in predict_function  *
        return step_function(self, iterator)
    File "C:\Users\ADM\Desktop\Marcelo\Developer\Projetos\lotofacil\lotofacil_exploracao\venv\lib\site-packages\keras\engine\training.py", line 2155, in step_function  **
        outputs = model.distribute_strategy.run(run_step, args=(data,))
    File "C:\Users\ADM\Desktop\Marcelo\Developer\Projetos\lotofacil\lotofacil_exploracao\venv\lib\site-packages\keras\engine\training.py", line 2143, in run_step  **
        outputs = model.predict_step(data)
    File "C:\Users\ADM\Desktop\Marcelo\Developer\Projetos\lotofacil\lotofacil_exploracao\venv\lib\site-packages\keras\engine\training.py", line 2111, in predict_step
        return self(x, training=False)
    File "C:\Users\ADM\Desktop\Marcelo\Developer\Projetos\lotofacil\lotofacil_exploracao\venv\lib\site-packages\keras\utils\traceback_utils.py", line 70, in error_handler
        raise e.with_traceback(filtered_tb) from None
    File "C:\Users\ADM\Desktop\Marcelo\Developer\Projetos\lotofacil\lotofacil_exploracao\venv\lib\site-packages\keras\engine\input_spec.py", line 298, in assert_input_compatibility
        raise ValueError(

    ValueError: Input 0 of layer "sequential" is incompatible with the layer: expected shape=(None, 15), found shape=(None, 14)
"""