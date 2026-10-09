"""Manual interno usado como única fonte de informação do chatbot.

O conteúdo é fictício e fica definido diretamente no código, como pede o desafio.
Cada seção tem um número para que o chatbot possa indicar de onde tirou a resposta
e palavras-chave (sinônimos) que ajudam a busca simples por palavras.
"""

EMPRESA = "NovaTech Soluções"

SECOES = [
    {
        "numero": 1,
        "palavras_chave": "horário, expediente, ponto, entrada, saída, almoço, atraso, hora extra",
        "titulo": "Horário de trabalho",
        "texto": (
            "O expediente padrão é de segunda a sexta-feira, das 8h às 17h, "
            "com 1 hora de intervalo para almoço. É permitida uma tolerância de "
            "15 minutos na entrada. O ponto deve ser registrado pelo aplicativo "
            "PontoNova, tanto na entrada quanto na saída. Horas extras só podem "
            "ser feitas com autorização prévia do gestor direto."
        ),
    },
    {
        "numero": 2,
        "palavras_chave": "home office, remoto, casa, trabalhar de casa, dias por semana",
        "titulo": "Trabalho remoto (home office)",
        "texto": (
            "Colaboradores com mais de 3 meses de empresa podem trabalhar em home "
            "office até 2 dias por semana. Os dias devem ser combinados com o "
            "gestor e registrados na agenda da equipe até a sexta-feira da semana "
            "anterior. Durante o home office, o colaborador deve estar disponível "
            "no chat corporativo durante todo o expediente."
        ),
    },
    {
        "numero": 3,
        "palavras_chave": "férias, folga, descanso, prazo, antecedência",
        "titulo": "Férias",
        "texto": (
            "As férias devem ser solicitadas pelo portal de RH com no mínimo 30 "
            "dias de antecedência. É possível dividir as férias em até 3 períodos, "
            "sendo que um deles deve ter pelo menos 14 dias corridos. O pedido "
            "precisa ser aprovado pelo gestor direto."
        ),
    },
    {
        "numero": 4,
        "palavras_chave": "reembolso, despesa, nota fiscal, viagem, refeição, prazo, valor, limite",
        "titulo": "Reembolso de despesas",
        "texto": (
            "Despesas de trabalho, como transporte para visitas a clientes e "
            "refeições em viagens, podem ser reembolsadas. O pedido deve ser feito "
            "no portal financeiro em até 10 dias após a despesa, com a nota fiscal "
            "anexada. O limite para refeições é de R$ 60,00 por dia. O pagamento "
            "do reembolso é feito junto com o salário do mês seguinte."
        ),
    },
    {
        "numero": 5,
        "palavras_chave": "equipamento, notebook, computador, headset, defeito, quebrado, perda, roubo, prazo",
        "titulo": "Equipamentos",
        "texto": (
            "Cada colaborador recebe um notebook e um headset no primeiro dia. "
            "Os equipamentos são de propriedade da empresa e devem ser devolvidos "
            "no desligamento. Em caso de defeito, perda ou roubo, o colaborador "
            "deve abrir um chamado no suporte de TI em até 24 horas."
        ),
    },
    {
        "numero": 6,
        "palavras_chave": "senha, segurança, tamanho da senha, e-mail suspeito, golpe, dois fatores",
        "titulo": "Segurança da informação",
        "texto": (
            "As senhas devem ter no mínimo 12 caracteres e ser trocadas a cada 90 "
            "dias. É proibido compartilhar senhas, inclusive com colegas de equipe. "
            "A autenticação em dois fatores é obrigatória no e-mail corporativo. "
            "E-mails suspeitos devem ser encaminhados para seguranca@novatech.com.br."
        ),
    },
    {
        "numero": 7,
        "palavras_chave": "suporte, TI, chamado, problema técnico, ramal",
        "titulo": "Suporte de TI",
        "texto": (
            "Chamados de TI são abertos pelo portal HelpNova ou pelo ramal 4000. "
            "O suporte funciona de segunda a sexta-feira, das 7h às 19h. Chamados "
            "urgentes, que impedem o trabalho, são atendidos em até 4 horas úteis."
        ),
    },
    {
        "numero": 8,
        "palavras_chave": "benefício, vale-refeição, plano de saúde, auxílio, valor, receber",
        "titulo": "Benefícios",
        "texto": (
            "A empresa oferece vale-refeição de R$ 35,00 por dia útil, plano de "
            "saúde sem coparticipação e auxílio home office de R$ 100,00 por mês "
            "para quem trabalha remotamente pelo menos 1 dia por semana. Os "
            "benefícios começam a valer a partir do primeiro dia de trabalho."
        ),
    },
    {
        "numero": 9,
        "palavras_chave": "roupa, vestimenta, traje, vestir",
        "titulo": "Vestimenta",
        "texto": (
            "O código de vestimenta é casual. Em reuniões presenciais com "
            "clientes, recomenda-se traje social ou esporte fino."
        ),
    },
    {
        "numero": 10,
        "palavras_chave": "treinamento, curso, integração, capacitação",
        "titulo": "Treinamentos",
        "texto": (
            "Todo novo colaborador deve concluir o treinamento de integração na "
            "plataforma AprendeNova durante a primeira semana. Os treinamentos de "
            "segurança da informação são obrigatórios e devem ser refeitos uma vez "
            "por ano."
        ),
    },
]


def manual_formatado():
    """Devolve o manual como texto, com cada seção numerada."""
    partes = [f"MANUAL INTERNO DA {EMPRESA.upper()}"]
    for secao in SECOES:
        partes.append(f"[Seção {secao['numero']}] {secao['titulo']}\n{secao['texto']}")
    return "\n\n".join(partes)
