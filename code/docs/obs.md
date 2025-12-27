Olá Pessoal!
Realizei esse teste de Backend. Construí uma api, seguindo os requisitos do sistema/caso.

Com a Linguagem Python e o framework Django + Drf, realizei o projeto no padrão MVT.

Motivo de escolha foi a capacidade de implementar um sistema com usuário genérico desaclopado
do Investidor, já que o django fornece um User Default, admin e sua
interface administrativa.

Além disso, o queryset e Orm do django auxilia bastante no desempenho das queries em funcao
das regras de negócio, caso existisse mais complexidade, era possível otimizar joins entre
tabelas.

O serializer do django, é o responsável pelos dados com validators e tratamentos que fa-
cilitam a produtividade do dev.

O Signals/Gatilho do django é essencial para o serviço externo SMTP que indicaram.

Portanto minha escolha, além da justificativa de conhecimento técnico em aprendizado
constante, deve também, a produtividade do django e sua abstração.

Dividi as entidades entre:
-Investidores
-Investimentos
-Usuarios

realizei o crud de investidores e de Investimentos.

em investimentos priorizei a seguranca de registros e usei uma flag booleana
para indicar o encerramento.


Futuramente, eu criaria perms e auth, para proteger o devido uso de cada Endpoint.
Além disso, seria interessante implementar talvez uma entidade Wallet
que assegurasse esses investimentos e métricas/business.

Utilizei também Libs auxiliares, todas estão nos requirements e na docs.

Para Format do código usei Ruff, tenho minhas manias e quero deixar padrão a leitura.
Para Task usei taskipy que facilita chamadas de tasks
Para Docs, usei MKdocs que ajuda no visual do Md(index)

Assegurei as Variáveis de Ambiente no .Env local.

Gostaria de um feedback, queria a opinião de vocês o que melhorariam e o que gostaram...
Obrigado, Prazer!