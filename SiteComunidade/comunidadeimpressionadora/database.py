from comunidadeimpressionadora import app, database
from comunidadeimpressionadora.models import Usuario, Post


#with app.app_context():
##################    database.drop_all() ###### CUIDADO COM ESSE COMANDO
#    database.create_all()



with app.app_context():
     #usuario11 = Usuario(username="usuario9", email="email11", senha="senha1234") # criando um usuario
     #database.session.add(usuario11) # salvando usuario no banco de dados
     #database.session.commit() # inserindo usuario no banco de dados

     meus_usuarios = Usuario.query.all() # retornando todos os usuarios do banco
     print(meus_usuarios) # imprimindo todos os usuarios
     primeiro_user = meus_usuarios[6] # retornando um usuario especifico da lista meus usuarios
     print(primeiro_user.username, primeiro_user.senha, primeiro_user.email) # imprimindo dados do usuario

     #buscando um usuario especifico
     #usuario_teste = Usuario.query.filter_by(id=2).first() # retornando com filtro especifico
     #print(usuario_teste) # escrevendo teste
     #print(usuario_teste.senha) # mostrando senha do usuario especifico no filter

     # criando um Post
     #meu_post = Post(id_usuario=2, titulo="titulo teste amor", corpo="o melhor do mundo acontece quando estavamos ao lado de um grande amor")
     #database.session.add(meu_post)
     #database.session.commit()

     #meus_post = Post.query.all()
     #print(meus_post)
     #primeiro_post = meus_post[2]
     #print(primeiro_post.autor.username)
     #print(primeiro_post.corpo)

#with app.app_context():
#    database.drop_all()
#    database.create_all()

