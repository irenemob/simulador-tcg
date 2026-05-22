# simulador-tcg
# Descrição inicial
> Esse programa é um protótipo de texto de um jogo de cartas, desenvolvido para o desafio da semana 2 da trilha de Python da for_code. Ele foi feito para praticar o desenvolvimento de funções, loops e condicionais, que foram o foco dessa semana.
> Ele funciona de forma simples: os jogadores digitam os seus nomes, pontos de ataque e de vida. O programa inicia, então, o duelo entre eles e roda até que um dos jogadores fique sem vida. 
> Condições importantes: De cara, pontos de ataque ou de vida negativos ou zerados não são permitidos. Após o duelo, pontos de vida negativos não são possíveis, e, então, são convertidos para 0 no resultado final. 
# Como rodar
> Basta copiar o codigo do repositório, abrir o gitbash , aplicar o comando "cd" para a pasta que deseja que o programa seja adicionado e aplicar o comando "git clone" com o link ao lado. Após isso, executar novamente o "cd" com o nome simulador-tcg ao lado, e abrir a pasta onde o programa está localizado no VSCODE. Então, basta rodar o código no terminal!
# Respostas das perguntas teóricas
> O laço "for" roda o código abaixo dele por um número DETERMINADO de vezes, enquanto o while roda indefinidamente até que a condição principal seja quebrada. O while é uma melhor escolha para esse projeto pois não é possível definir, nesse modelo de jogo, de cara um número de rodadas. Esse número será o necessário para que um dos monstros fique sem vida. Isso se encaixa exatamente na proposta do "while". 
> A palavra return é o que faz com que a operação da função seja efetivamente realizada. Em caso de operações matemáticas sem o return, o computador armazenará a operação mas não a realizará.
> Ocorre quando o código abaixo do while não encerra nunca, e o programa roda infinitamente no computador, o que gera problemas, como bugs. Ele é evitado ao se colocar uma condição principal no loop, que, quando não for mais cumprida, fará ele encerrar automaticamente. No caso do programa, é a condição da vida dos monstros ser maior do que 0. O loop (que é o jogo em si) roda até que um dos monstros morra. Para isso, dentro do loop, a vida deve ser atualizada conforme as batalhas. 

