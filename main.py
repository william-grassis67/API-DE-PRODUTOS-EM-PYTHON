from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

class Produto(BaseModel):
    nome: str
    descricao: str
    preco: float
    qtd: int

proximo_id = 1
produtos=[]

app = FastAPI()

app.add_middleware (
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def inicio():
    return {
        "menssagem": "Olá seja bem-vindo(a) a minha API feita em python!"
    }

@app.get("/produtos")
def listar_tarefas():
    return produtos 



@app.post("/register/tarefa")
def registrar_produto(produto: Produto):
    global proximo_id

    if not produto.nome.strip() or not produto.descricao.strip():
        return {"mensagem": "Nome e descrição são obrigatórios!"}

    if produto.preco <= 0 or produto.qtd < 1:
        return {"mensagem": "Preço e quantidade devem ser maiores que zero!"}

    novo_produto = {
        "id": proximo_id,
        "nome": produto.nome,
        "descricao": produto.descricao,
        "preco": produto.preco,
        "quantidade": produto.qtd,
    }

    produtos.append(novo_produto)
    proximo_id += 1

    return novo_produto



@app.put("/update/{produto_id}")
def atualizar_produto(produto_id: int, dados: Produto):
    for produto in produtos:
        if produto["id"] == produto_id:
            produto["nome"] = dados.nome

            # Atualize aqui:
            # descricao
            # preco
            # quantidade

            # Retorne o produto atualizado aqui

    # Se não encontrar o produto, trate o erro
