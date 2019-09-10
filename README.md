# projeto-so
Projeto de processos, memória compartilhada e sincronização

# What is it?

Definimos uma função **unroll** que recebe uma matriz(LxN) de valores, **args**; uma função, **func**, que deve ser chamada em paralelo; uma lista de retornos, **results**, que deve ser usado para armazenar os retornos da função *func*, se existirem; um parâmetro, **method**, que é usado para indicar o tipo de implementação paralela que será usada. Cada linha, *l*, da matriz args representa uma chamada de *func*. Os parâmetros de cada chamada de func serão os elementos das linhas da matriz *args*, quando *func* retorna alguma coisa, esse retorno deve ser armazenado na lista *results*. O Parâmetro *method* indica se *unroll* irá implementar o paralelismo das chamadas de *func* usando threads.

Além disso, implementamos um programa sequencial para calcular as mesmas operações em matrizes que foram realizadas pelo programa paralelo. Adicionamos ao programa paralelo e ao sequencial uma biblioteca do *python* chamada **time** para calcular o tempo de execução das chamadas de função em paralela e das sequenciais para comparar.

Feito isso, geramos um gráfico com o tempo de execução de determinados tamanhos de matrizes da sequencial e da thread (execução em paralelo).

É possível ver os gráficos de demais comentários no relatório [aqui.](https://docs.google.com/document/d/1G9IJ7R0-e910tZOYGsLDwndf7WHOZGaDABPCzTYLszU/)
