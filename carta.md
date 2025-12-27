Olá, pessoal.

Realizei este teste de Backend, no qual construí uma API seguindo os requisitos propostos no sistema/caso apresentado.

Utilizei a linguagem Python em conjunto com o framework Django e Django Rest Framework (DRF), estruturando o projeto no padrão MVT.

A escolha do Django se deu principalmente pela possibilidade de implementar um sistema com um usuário genérico desacoplado da entidade Investidor, aproveitando o User padrão fornecido pelo framework, bem como sua interface administrativa nativa.

Além disso, o ORM e os querysets do Django auxiliam significativamente no desempenho das consultas, especialmente considerando as regras de negócio envolvidas. Em um cenário de maior complexidade, seria possível otimizar ainda mais as queries, incluindo joins entre tabelas de forma eficiente.

Os serializers do Django foram utilizados como responsáveis pelo tratamento e validação dos dados, o que contribui diretamente para a produtividade do desenvolvedor e para a segurança da aplicação.

Os Signals (gatilhos) do Django foram empregados como parte essencial da integração com o serviço externo de SMTP, conforme solicitado nos requisitos.

Portanto, a escolha da stack não se deu apenas por afinidade técnica ou aprendizado contínuo, mas também pela produtividade, organização e nível de abstração que o Django oferece.

As entidades foram divididas em:

- Usuários

- Investidores

- Investimentos

Foi implementado o **CRUD** completo para Investidores e Investimentos.

No caso dos investimentos, priorizei a segurança e a integridade dos registros, utilizando uma flag booleana para indicar o encerramento, evitando alterações indevidas em registros históricos.

Como melhorias futuras, considero a implementação de permissões e autenticação mais refinadas, garantindo o uso adequado de cada endpoint. Além disso, seria interessante a criação de uma entidade Wallet, responsável por consolidar os investimentos, métricas e regras de negócio relacionadas.

Também utilizei bibliotecas auxiliares, todas devidamente documentadas no arquivo de requirements e na documentação do projeto.

Para padronização e formatação do código, utilizei o Ruff, visando manter um padrão de leitura consistente, tento sempre seguir padrão python, mas tenho costumes de aspas e outros toques.
Para automação de tarefas, utilizei o Taskipy, facilitando a execução de comandos recorrentes. Para documentação, utilizei o MkDocs, buscando uma melhor organização e visualização dos arquivos Markdown.

As variáveis de ambiente foram devidamente protegidas e configuradas por meio de um arquivo .env local.

Fico à disposição para receber feedbacks. Gostaria muito de ouvir a opinião de vocês sobre pontos de melhoria e aspectos positivos do projeto.

Agradeço pela oportunidade, Prazer!