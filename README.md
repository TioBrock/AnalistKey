# AnalistKey - Analisador de Senhas

Este projeto é um analisador de senhas desenvolvido em Python para **verificação de senhas** e **geração de senhas seguras**. Ele aplica critérios de segurança e fornece análises simples.

---

## Funcionalidades

- Avalia a força da senha
- Detecta padrões comuns com regex
- Geração de senhas seguras com tamanho personalizado
- Estimativa aproximada de tempo necessário para ser descoberta em um ataque bruteforce simples
- Interface de terminal
- Escrito em Python puro (apenas bibliotecas padrão)

---

## Boas Práticas para Criar Senhas

- **Use no mínimo 8 caracteres**, preferencialmente 12 ou mais.
- Misture **letras maiúsculas, minúsculas, números e símbolos**.
- Evite usar informações óbvias como nomes, datas de nascimento, palavras ou comuns (ferramentas de quebra de senha que utilizam machine learning buscam usar essas informações e padrões comuns)
- **Não reutilize senhas** em diferentes contas.
- Prefira senhas aleatórias ou geradas por geradores de senha.
- Armazene suas senhas em um **gerenciador seguro de senhas**, ou em um papel que você não vá perder.
- Atualize senhas antigas ou expostas periodicamente.

---

## Critérios de avaliação

A senha recebe pontos conforme os seguintes requisitos:

- Mínimo de 8 caracteres
- Pelo menos uma letra **maiúscula**
- Pelo menos uma letra **minúscula**
- Presença de **números**
- Presença de **caracteres especiais**
- Não seguir padrões comuns (ex: `senha123`, `vasco@1998`, etc.)

A nota final varia entre 0 e 6 pontos. A entropia é usada para estimar o tempo que um ataque de força bruta levaria para descobrir a senha.

---

## Cálculo de entropia

O cálculo é feito com base no tamanho da senha e no tamanho do conjunto de caracteres utilizado (maiúsculas, minúsculas, números e símbolos). O valor de **1.500.000 tentativas por segundo**, foi colocado pois é o que um hardware médio faria.

A fórmula aplicada é:

```

Entropia = log2(possibilidades) × tamanho da senha
Tempo ≈ 2^entropia / tentativas por segundo

```

---

## Execução

Requisitos:
- Python 3.6+

## Tecnologias Utilizadas

* Linguagem: `Python`
* Bibliotecas padrão:

  * `re`
  * `math`
  * `random`
  * `os`

Não é necessário instalar nenhuma dependência.

---

## Licença

Este projeto está licenciado sob os termos da **MIT License**. Veja o arquivo `LICENSE` para mais informações.

---

## Autor

Desenvolvido por **Tio Brock** com o objetivo de auxiliar na construção de uma senha segura, aprendizado, segurança da informação e boas práticas de desenvolvimento.

Sinta-se à vontade para sugerir melhorias e para reutilizar meu programa. <3
