# python-dijkstra
MC346 Unicamp - Projeto 3 (Python) :: http://www.ic.unicamp.br/~wainer/cursos/2s2019/346/proj-python.html

Escreva um programa em Python que vai calcular o caminho mais rápido (e o segundo mais rápido) na média entre uma origem em um destino dado. O programa recebe um grafo direcionado e informação sobre a distancia e velocidade máxima na aresta, e recebe também várias medições sobre a velocidade real das arestas deve calcular o cominho mais rápido na média e o segundo mais rápido na média (assumindo que o motorista andará na maior velocidade permitida em cada aresta) entre uma origem e um destino dados. 

Input Model:
```
25.0
aa b 0.4
aa c 0.5 50.0
b d 1.2
b z 0.2 
z f4 0.3 40.0

aa b 12.5 11.3 10.2 15.3 12.0
aa c 4.1 4.3 4.7
z f4 19.0
b z 0 
aa
z
```

A primeira linha indica a velocidade máxima default nas ruas da cidade, neste caso, se não ha indicação de velocidade máxima na rua, assume-se que seja 25k/h e que o motorista vai dirigir a 25 k/h

As linhas seguintes são as arestas direcionadas que possuem 3 ou quatro valores. Os dois primeiros são os vértices. O terceiro valor é a distancia em quilômetros entre os vértices. Se houver um quarto valor ele é a velocidade máxima naquele trecho e naquele sentido. O fato da velocidade máxima entre a e c ser 50k/h não significa que ele seja a velocidade no sentido de c para a. Na verdade pode não haver uma aresta de c para a (ou seja esse trecho da rua é mão única).

Ao final do grafo haverá uma linha sem dados. A partir deste ponto os dados indicam diferentes medidas de velocidades atuais nas arestas. Nos últimos 10 minutos, a velocidade de usuários do Waze de aa para b foram medidas como 12.5, 11.3, 10.2, 15.3 e 12.0 k/h. O sistema assume que alguma as dessas sejam a velocidade máxima (neste momento) nessas arestas. Note que nem todas as arestas terão uma linha de atualização da sua velocidade real. Note também que algumas ruas podem ter velocidade máxima de 0k/h ou seja a rua esta fechada e aquela aresta temporariamente não existe.

Finalmente haverá duas linhas com a origem (aa) e o destino (z).

Calcule o caminho mais rápido (na média) e o segundo mais rapido (como alternativa p/ o motorista) o entre a origem e o destino. 
