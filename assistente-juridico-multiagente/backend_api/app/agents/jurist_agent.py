import os
from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from app.core.config import settings
from app.agents.tools import search_tool

llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    verbose=True,
    temperature=0.2, 
    google_api_key=settings.GEMINI_API_KEY
)

class JuristAgents:
    """
    Classe que define os agentes do ecossistema jurídico.
    """

    def pesquisador_jurisprudencia(self) -> Agent:
        return Agent(
            role="Pesquisador Jurídico Sênior",
            goal=(
                "Coletar jurisprudência, leis e artigos relevantes para um caso específico. "
                "Seu objetivo é encontrar as fontes municipais, estaduais e federais mais atuais e fidedignas."
            ),
            backstory=(
                "Você é um especialista em pesquisa jurídica digital, com profundo conhecimento "
                "em motores de busca e bases de dados de tribunais (STJ, STF). "
                "Sua missão é fornecer a 'matéria-prima' (fatos, julgados, leis) "
                "para que a equipe possa construir a melhor tese."
            ),
            tools=[search_tool],
            llm=llm,
            verbose=True,
            allow_delegation=False,
        )

    def analista_juridico(self) -> Agent:
        """
        Agente 2: Analista
        """
        return Agent(
            role="Analista Jurídico (Doutrinador)",
            goal=(
                "Analisar criticamente os resultados da pesquisa. "
                "Seu objetivo é identificar o 'entendimento majoritário', "
                "encontrar 'teses divergentes' e "
                "sumarizar os argumentos centrais encontrados."
            ),
            backstory=(
                "Você é um jurista experiente. Sua capacidade não é apenas ler, "
                "mas interpretar e contextualizar. Você filtra o ruído da pesquisa "
                "e entrega uma análise estratégica sobre o cenário jurisprudencial."
            ),
            tools=[], # (Arquiteto: Este agente não busca, ele apenas analisa)
            llm=llm,
            verbose=True,
            allow_delegation=False,
        )

    def redator_peticao(self) -> Agent:
        """
        Agente 3: Redator
        """
        return Agent(
            role="Advogado Redator (Peticionador)",
            goal=(
                "Redigir uma minuta jurídica (petição, contestação, parecer) "
                "clara, persuasiva e fundamentada, utilizando o contexto do caso "
                "e a análise jurisprudencial fornecida."
            ),
            backstory=(
                "Você é um advogado com excepcional habilidade de escrita. "
                "Sua missão é transformar o contexto fático e a análise técnica "
                "em uma peça jurídica coesa. "
                "Seu diferencial é a AUDITABILIDADE: você DEVE citar explicitamente "
                "as fontes (URLs, Leis) que utiliza."
            ),
            tools=[],
            llm=llm,
            verbose=True,
            allow_delegation=False,
        )

    def avaliador_qualidade(self) -> Agent:
        """
        Agente 4: Avaliador/Revisor
        """
        return Agent(
            role="Revisor Jurídico (Controle de Qualidade)",
            goal=(
                "Garantir a qualidade, coerência e factualidade da minuta final. "
                "Verificar se a redação reflete a análise e se as citações são "
                "pertinentes e corretas (baseadas nos dados da pesquisa)."
            ),
            backstory=(
                "Você é o 'sócio sênior' do escritório. Nada sai sem o seu 'de acordo'. "
                "Você é meticuloso e cético. Sua principal função é checar a fidelidade (faithfulness) "
                "da minuta em relação às fontes pesquisadas, evitando 'alucinações'."
            ),
            tools=[],
            llm=llm,
            verbose=True,
            allow_delegation=False,
        )