# plataforma/management/commands/inserir_dados.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from plataforma.models import Categoria, Noticia
from datetime import datetime

class Command(BaseCommand):
    help = 'Insere categorias iniciais no banco de dados'

    def handle(self, *args, **kwargs):
        self.inserir_categorias()
        self.inserir_noticias()
        self.criar_usuarios()
    
    def criar_usuarios(self):
        print("Criando usuários...")

        # Criar usuário admin
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@gmail.com',
                password='admin1234' 
            )
            print("Usuário admin criado com sucesso!")
        else:
            print("O usuário admin já existe.")

        # Criar usuário staff
        if not User.objects.filter(username='Silvia Cognatto').exists():
            user_staff = User.objects.create_user(
                username='Silvia Cognatto',
                email='silvia.cog@gmail.com',
                password='123456789' 
            )
            user_staff.is_staff = True
            user_staff.save()
            print("Usuário Silvia Cognatto criado com sucesso!")
        else:
            print("O usuário staff já existe.")
            
    def inserir_categorias(self):
        print("Verificando se as categorias existem...")
        dados = [
            {"nome": "Educação"},
            {"nome": "Empreendedorismo"},
            {"nome": "Empregabilidade"},
            {"nome": "Força feminina"},
            {"nome": "Programação"},
            {"nome": "Educação"},
            {"nome": "Empreendedorismo"},
            {"nome": "Diversidade"},
            {"nome": "Mulheres inspiradoras"},
        ]
        
        for dado in dados:
            if not Categoria.objects.filter(nome=dado["nome"]).exists():
                instancia = Categoria(**dado)
                instancia.save()
                print(f"Categoria '{dado['nome']}' inserida com sucesso!")
            else:
                print(f"A categoria '{dado['nome']}' já existe.")
        self.stdout.write(self.style.SUCCESS("Inserção de dados concluída com sucesso."))

    def inserir_noticias(self):
        print("Verificando se as notícias existem...")
        
        
        categoria_empregabilidade = Categoria.objects.get(id=1) 
        categoria_forca_feminina = Categoria.objects.get(id=2) 
        categoria_programacao = Categoria.objects.get(id=3) 
        categoria_educacao = Categoria.objects.get(id=4)
        categoria_empreendedorismo= Categoria.objects.get(id=5)
        categoria_diversidade= Categoria.objects.get(id=6)
        categoria_mulheres_inspiradoras= Categoria.objects.get(id=7)
        
        autor_silvia = User.objects.get(id=1)

        # Dados da notícia
        noticias_dados = [
            {
                "titulo": "Novas perspectivas estão chegando!",
                "subtitulo": "Empresas estão apoiando a inclusão de pessoas trans no mercado de trabalho",
                "conteudo": "<p>Nos últimos anos, a discussão sobre diversidade e inclusão no ambiente de trabalho ganhou destaque, \
                            e um dos focos importantes dessa conversa é a inclusão de mulheres trans. Com a crescente conscientização sobre a \
                            importância de um ambiente de trabalho diverso, muitas empresas estão implementando iniciativas para apoiar a entrada e\
                            o desenvolvimento profissional de mulheres trans, especialmente no setor de tecnologia.</p><h2>Apoios e Iniciativas</h2>\
                            <p>Iniciativas como programas de capacitação, mentoria e políticas de recrutamento inclusivas estão se tornando comuns entre as empresas \
                            de tecnologia. Por exemplo, a ThoughtWorks, uma consultoria de tecnologia, lançou um programa de treinamento específico para mulheres \
                            trans e não-binárias, visando prepará-las para cargos na área de tecnologia. O programa inclui workshops técnicos, desenvolvimento \
                            de soft skills e orientação sobre o mercado de trabalho.</p><p>Outra empresa que se destacou nessa área é a Accenture, \
                            que implementou uma política de recrutamento inclusiva, focada em aumentar a diversidade de gênero em sua força de trabalho. \
                            A Accenture também realiza parcerias com organizações LGBTQIA+, oferecendo suporte a mulheres trans em suas trajetórias profissionais.</p>\
                            <h2>Mudanças Culturais e Estruturas de Apoio</h2>\
                            <p>Além das iniciativas de contratação, as empresas estão cada vez mais cientes da necessidade de criar um ambiente acolhedor \
                            para seus colaboradores. Isso inclui a promoção de uma cultura organizacional que valorize a diversidade e a inclusão, \
                            garantindo que mulheres trans se sintam seguras e apoiadas no ambiente de trabalho. Políticas como a implementação de banheiros \
                            unissex e a promoção de treinamentos sobre diversidade para todos os funcionários são exemplos de como as empresas estão trabalhando para criar um espaço mais inclusivo.</p>\
                            <h2>Desafios Persistentes</h2><p>Apesar dos avanços, ainda existem desafios significativos. \
                            Mulheres trans frequentemente enfrentam barreiras como preconceito e discriminação no ambiente de trabalho. \
                            O relatório de 2024 da Fundação Getúlio Vargas aponta que a taxa de desemprego entre pessoas trans é significativamente maior do que a \
                            média nacional. Esse cenário evidencia a necessidade de esforços contínuos para garantir que as iniciativas de inclusão sejam eficazes \
                            e que mulheres trans tenham acesso igualitário às oportunidades no mercado de trabalho.</p>\
                            <p><img src='https://img.freepik.com/fotos-gratis/vista-lateral-de-uma-pessoa-lesbica-no-trabalho_23-2150617777.jpg?t=st=1730305527~exp=1730309127~hmac=7bca65ebb8811700d85b21abba43a8ce348f7da3c11b946b00fb0c8b4cf492fd&amp;w=1380' class='responsive-image'></p>\
                            <h2>Um Futuro Promissor</h2> \
                            <p>No entanto, as perspectivas são encorajadoras. Com o aumento do ativismo e a pressão da sociedade civil por uma maior inclusão, muitas empresas \
                            estão se comprometendo a melhorar suas práticas. O movimento pela igualdade de gênero e diversidade está se tornando uma prioridade estratégica \
                            para muitas organizações, levando a um ambiente de trabalho mais justo e equitativo.</p>\
                            <p>A inclusão de mulheres trans no mercado de trabalho, especialmente em setores como tecnologia, não apenas enriquece o \
                            ambiente corporativo, mas também é fundamental para a construção de uma sociedade mais justa. À medida que as empresas continuam \
                            a adotar práticas inclusivas, espera-se que mais mulheres trans tenham a oportunidade de contribuir com suas habilidades e \
                            talentos em um setor em rápida evolução.</p>",
                "capa": "noticias/arte_diversidade.png",  
                "categoria": categoria_diversidade,
                "autor": autor_silvia,
                "status": "PU",  
                "data_publicacao": datetime.now()
            },
            {
                "titulo": "Cresce a Participação Feminina na Tecnologia em 2024",
                "subtitulo": "Iniciativas e exemplos inspiradores impulsionam a entrada e ascensão das mulheres em um dos setores mais promissores do mercado.",
                "conteudo":"<article><p>Em 2024, o setor de tecnologia testemunhou um crescimento notável na empregabilidade das mulheres, refletindo um esforço contínuo para promover a diversidade e a inclusão. De acordo com o relatório da Tech Workforce Initiative, a participação feminina nas funções tecnológicas atingiu 35%, um aumento de 5%/ em relação ao ano anterior.</p><br>\
                            <p>Os dados também mostram que as mulheres estão cada vez mais ocupando cargos de liderança. O número de mulheres em posições de gestão cresceu 10% desde 2023, agora representando 30% dos cargos executivos nas principais empresas de tecnologia. Esse aumento é atribuído a iniciativas como programas de mentoria e treinamento focados em desenvolvimento de carreira para mulheres.</p><br>\
                            <p><img src='https://img.freepik.com/free-photo/programming-background-concept_23-2150170137.jpg?t=st=1730305210~exp=1730308810~hmac=2cf8c11dc5a3c9cddaecffa77f0cca67da74f4652bbe74e404414d48dbc599b1&amp;w=1380' class='responsive-image'></p>\
                            <p>Além disso, a pesquisa aponta que as mulheres são mais propensas a trabalhar em áreas emergentes como inteligência artificial e ciência de dados. Em 2024, cerca de 40% dos novos profissionais contratados nessas áreas eram mulheres, um avanço significativo em um setor historicamente dominado por homens.</p><br>\
                            <p>Apesar do progresso, desafios persistem. A pesquisa revelou que as mulheres ainda enfrentam barreiras significativas, como a falta de representatividade em certas áreas tecnológicas e disparidades salariais. O relatório indica que as mulheres na tecnologia ganham em média 15% a menos que seus colegas homens.</p><br>\
                            <p>A Tech Workforce Initiative conclui que, embora os avanços sejam encorajadores, ainda há muito a ser feito para garantir que as mulheres tenham igualdade de oportunidades e salários justos no setor de tecnologia. As empresas são incentivadas a continuar investindo em programas de diversidade e inclusão para apoiar a carreira das mulheres na tecnologia.</p><br>\
                            </article>",
                "capa": "noticias/tela_codigos.png",  
                "categoria": categoria_empregabilidade,
                "autor": autor_silvia,
                "status": "PU",
                "data_publicacao": datetime.now()
            },
            {
                "titulo": "Mulheres em Cargos de Liderança no Brasil",
                "subtitulo": "Aumento da presença feminina redefine o cenário de liderança em setores historicamente dominados por homens.",
                "conteudo":"<article><p>Em 2024, o setor de tecnologia testemunhou um crescimento notável na empregabilidade das mulheres, refletindo um esforço contínuo para promover a diversidade e a inclusão. De acordo com o relatório da Tech Workforce Initiative, a participação feminina nas funções tecnológicas atingiu 35%, um aumento de 5% em relação ao ano anterior.</p><br>\
                            <p>Os dados também mostram que as mulheres estão cada vez mais ocupando cargos de liderança. O número de mulheres em posições de gestão cresceu 10% desde 2023, agora representando 30% dos cargos executivos nas principais empresas de tecnologia. Esse aumento é atribuído a iniciativas como programas de mentoria e treinamento focados em desenvolvimento de carreira para mulheres.</p><br>\
                            <p>Além disso, a pesquisa aponta que as mulheres são mais propensas a trabalhar em áreas emergentes como inteligência artificial e ciência de dados. Em 2024, cerca de 40% dos novos profissionais contratados nessas áreas eram mulheres, um avanço significativo em um setor historicamente dominado por homens.</p><br>\
                            <p>Apesar do progresso, desafios persistem. A pesquisa revelou que as mulheres ainda enfrentam barreiras significativas, como a falta de representatividade em certas áreas tecnológicas e disparidades salariais. O relatório indica que as mulheres na tecnologia ganham em média 15% a menos que seus colegas homens.</p><br>\
                            <p>A Tech Workforce Initiative conclui que, embora os avanços sejam encorajadores, ainda há muito a ser feito para garantir que as mulheres tenham igualdade de oportunidades e salários justos no setor de tecnologia. As empresas são incentivadas a continuar investindo em programas de diversidade e inclusão para apoiar a carreira das mulheres na tecnologia.</p><br>\
                            </article>",
                "capa": None,  
                "categoria": categoria_empregabilidade,
                "autor": autor_silvia,
                "status": "AN",
                "data_publicacao": datetime.now()
            },
            {
                "titulo": "Katherine Johnson: Pioneira da Matemática na NASA",
                "subtitulo": "A trajetória de uma mulher que desafiou normas e ajudou a conquistar o espaço com seus cálculos precisos.",
                "conteudo":"<p>Katherine Johnson, uma matemática afro-americana cuja carreira na NASA ajudou a moldar a exploração espacial, tornou-se um ícone de resistência e excelência em um campo dominado por homens brancos. Nascida em 26 de agosto de 1918, em White Sulphur Springs, West Virginia, Johnson desafiou as normas sociais e raciais de sua época, superando barreiras para se tornar uma das mentes mais brilhantes da engenharia e da matemática.</p><br>\
                            <h2>Educação e Carreira Inicial</h2>\
                            <p>Desde jovem, Katherine demonstrou um talento excepcional para matemática. Com apenas 14 anos, ela se formou no ensino médio e começou seus estudos na West Virginia University, onde foi uma das primeiras mulheres afro-americanas a se matricular na instituição. Após concluir sua graduação em matemática e francês, Johnson começou sua carreira na Navy Reserve, onde fez cálculos para missões de voo.</p>\
                            <p>Em 1953, Katherine se juntou ao Langley Research Center da NASA, onde se destacou em um ambiente que era, na época, quase totalmente masculino e predominantemente branco.</p>\
                            <p><img src='https://s2.glbimg.com/4x46Vk0od7TNL00eJcBMbB1n7eE=/e.glbimg.com/og/ed/f/original/2020/02/24/katherine_johnson_john_glenn_0.png' class='responsive-image'></p>\
                            <h2>Contribuições para a Exploração Espacial</h2>\
                            <p>Johnson é mais conhecida por seus cálculos de trajetória para o primeiro voo orbital dos Estados Unidos, realizado por John Glenn em 1962. Em um momento crucial, quando os computadores ainda eram novos e não totalmente confiáveis, Glenn pediu que os cálculos de seu voo fossem verificados por Johnson. Sua confiança nos cálculos da matemática foi um testemunho da precisão e da importância de seu trabalho.</p>\
                            <p>Além disso, Katherine desempenhou um papel fundamental nas missões de Apollo, incluindo o histórico pouso na Lua em 1969. Seus cálculos foram essenciais para garantir que os astronautas pudessem voltar com segurança à Terra, solidificando seu legado na história da NASA.</p>\
                            <h2>Reconhecimento e Legado</h2>\
                            <p>Apesar de suas contribuições significativas, Katherine Johnson não recebeu o reconhecimento que merecia durante sua vida. No entanto, o cenário começou a mudar em 2015, com o lançamento do livro <em>Hidden Figures</em> (Estrelas além do tempo) e sua adaptação cinematográfica. O filme destacou as histórias de mulheres afro-americanas que contribuíram para o programa espacial, trazendo à tona a vida e a carreira de Johnson e suas colegas, Dorothy Vaughan e Mary Jackson.</p>\
                            <p>Em 2016, Johnson recebeu a Medalha Presidencial da Liberdade, um dos mais altos honrarias civis nos Estados Unidos, e em 2020, ela se tornou a primeira mulher a ter sua própria área homenageada na NASA, quando o prédio de engenharia foi renomeado em sua honra.</p>\
                            <p><img src='https://upload.wikimedia.org/wikipedia/commons/2/22/Katherine_Johnson_medal.jpeg' class='responsive-image'></p>\
                            <h2>A Inspiração que Deixou</h2>\
                            <p>Katherine Johnson faleceu em 24 de fevereiro de 2020, mas seu legado vive. Sua história é uma inspiração para muitas mulheres e pessoas de cor que aspiram a seguir carreiras em ciência, tecnologia, engenharia e matemática (STEM). Ela não apenas quebrou barreiras em seu campo, mas também se tornou um símbolo de perseverança e excelência.</p>\
                            <p>Hoje, Katherine Johnson é lembrada como uma das figuras mais influentes na história da NASA e um exemplo de como a determinação e o talento podem mudar o mundo, desafiando preconceitos e preconceitos de gênero e raça.</p>\
                            </article>",
                "capa": "noticias/Katherine_johnson.png",  
                "categoria": categoria_mulheres_inspiradoras,
                "autor": autor_silvia,
                "status": "PU",
                "data_publicacao": datetime.now()
            },
            {
                "titulo": "O caminho começa hoje!",
                "subtitulo": "Ensinar habilidades essenciais para empoderar meninas e prepará-las para um futuro de sucesso e igualdade.",
                "conteudo":"<article><h1>Empoderar Meninas para um Futuro Brilhante</h1>\
                        <p>Empoderar meninas para que se tornem mulheres fortes e autoconfiantes é um desafio que demanda um esforço coletivo. O que precisamos ensinar para que as futuras gerações de mulheres sejam resilientes, independentes e capazes de superar obstáculos? Aqui estão algumas lições essenciais que devem ser incorporadas na educação e no cotidiano das meninas.</p><br>\
                        <h2>1. Autoconfiança e Autoestima</h2>\
                        <p>Uma das habilidades mais importantes que devemos cultivar é a autoconfiança. Desde pequenas, as meninas devem ser encorajadas a acreditar em si mesmas e em suas capacidades. Isso pode ser feito através de elogios sinceros e feedback positivo, além de exposições a atividades que desenvolvam suas habilidades e talentos. Incentivar as meninas a enfrentar desafios e a celebrar suas conquistas, por menores que sejam, ajuda a construir uma autoestima sólida.</p><br>\
                        <h2>2. Educação Financeira</h2>\
                        <p>Ensinar sobre finanças desde cedo é crucial para a independência futura. As meninas devem aprender sobre gestão de dinheiro, como poupar, investir e fazer escolhas financeiras inteligentes. Compreender o valor do dinheiro e como usá-lo de forma consciente empodera as mulheres a tomarem decisões financeiras que afetarão suas vidas de maneira significativa.</p><br>\
                        <h2>3. Resiliência e Habilidades de Solução de Problemas</h2>\
                        <p>A vida está repleta de desafios e obstáculos. Ensinar as meninas a serem resilientes e a enfrentarem dificuldades com coragem é fundamental. Promover habilidades de solução de problemas, como pensar criticamente e encontrar soluções criativas, pode prepará-las para lidar com situações difíceis. Isso inclui ensiná-las a ver o fracasso como uma oportunidade de aprendizado, em vez de um fim.</p><br>\
                        <h2>4. Importância da Educação e da Formação Contínua</h2>\
                        <p>A educação é uma ferramenta poderosa que pode abrir portas e criar oportunidades. Incentivar as meninas a valorizarem a educação e a buscarem conhecimento em diferentes áreas, seja em ciências, artes ou esportes, é essencial. Além disso, mostrar a importância da formação contínua, como cursos e workshops, as prepara para um mercado de trabalho em constante evolução.</p><br>\
                        <h2>5. Autonomia e Tomada de Decisões</h2>\
                        <p>As meninas devem ser incentivadas a serem autônomas e a tomarem decisões informadas. Isso envolve dar a elas a liberdade de escolher suas atividades, amigos e interesses, respeitando suas opiniões e promovendo um ambiente onde possam expressar suas ideias. Ensinar sobre a importância de ouvir a si mesmas e confiar em suas intuições contribui para a formação de mulheres decididas e autoconfiantes.</p><br>\
                        <h2>6. Solidariedade e Empatia</h2>\
                        <p>Construir uma rede de apoio entre mulheres é fundamental para a força feminina. Ensinar as meninas a serem solidárias, empáticas e a valorizarem as conquistas umas das outras promove um ambiente de colaboração. Elas devem aprender a importância de apoiar e encorajar outras mulheres, reconhecendo que o sucesso não diminui o espaço de ninguém.</p><br>\
                        <h2>7. Consciência sobre Igualdade de Gênero</h2>\
                        <p>Instruir sobre igualdade de gênero e os desafios que as mulheres enfrentam na sociedade é crucial. Isso inclui discutir questões como discriminação, violência de gênero e desigualdade salarial. Ter uma compreensão crítica dessas questões ajuda as meninas a se tornarem defensoras dos direitos das mulheres e a lutarem por um mundo mais justo.</p><br>\
                        <h2>Conclusão</h2>\
                        <p>Preparar meninas para se tornarem mulheres fortes requer um esforço conjunto entre famílias, escolas e a sociedade como um todo. Ao promover a autoconfiança, a educação financeira, a resiliência, a autonomia e a empatia, podemos formar gerações de mulheres preparadas para enfrentar desafios, conquistar seus sonhos e fazer a diferença no mundo. O futuro depende da força e da determinação das mulheres que estão se formando hoje.</p><br>\
                        </article>",
                "capa": "noticias/meninas_telas.png",  
                "categoria": categoria_educacao,
                "autor": autor_silvia,
                "status": "PU",
                "data_publicacao": datetime.now()
            },
        ]
        
        for dado in noticias_dados:
            if not Noticia.objects.filter(titulo=dado["titulo"]).exists():
                instancia = Noticia(**dado)
                instancia.save()
                print(f"Notícia '{dado['titulo']}' inserida com sucesso!")
            else:
                print(f"A notícia '{dado['titulo']}' já existe.")
        self.stdout.write(self.style.SUCCESS("Inserção de notícias concluída com sucesso."))