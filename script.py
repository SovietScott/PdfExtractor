import os, shutil, glob, sys, logging
import fitz
from tqdm import tqdm

workdir = f"{os.getcwd()}/pdf" # diretório dos pdfs
output = f"{os.getcwd()}/imagens" #diretório que serão armazenadas as imagens

logging.basicConfig(
    level=logging.DEBUG,
    format="{asctime} {levelname:<8} {message}",
    style='{',
    filename='%slog' % __file__[:-2],
    filemode='w'
)

def extract_image(pdf_dir, img_dir):
    try:
        for arquivo in os.listdir(pdf_dir):
            if ".pdf" in arquivo:
                diretorio_novo = f"{img_dir}/{arquivo[:-3]}"
                os.mkdir(diretorio_novo)

                doc = fitz.Document((os.path.join(pdf_dir, arquivo)))

                try:
                    for i in tqdm(range(len(doc)), desc="páginas"):
                        for img in tqdm(doc.get_page_images(i), desc="imagens da página"):
                            xref = img[0]
                            pix = fitz.Pixmap(doc, xref)
                            if not pix.colorspace.name in (fitz.csGRAY.name, fitz.csRGB.name):
                                pix = fitz.Pixmap(fitz.csRGB, pix)
                            pix.save(os.path.join(diretorio_novo, "%s_p%s-%s.png") % (arquivo[:-4], i, xref))
    
                    print("Processo concluído!")
                    logging.info("O processo executou como esperado para todos os arquivos")

                except Exception as e:
                    print(f"Algo deu errado no processamento do último pdf listado aqui! \n {e}")
                    logging.error("O processamento falhou em algum dos arquivos na fila")

    except Exception as e:
        print(f"Ocorreu um erro, talvez você esqueceu de criar os caminhos de entrada e saída ou os esses diretórios já estão populados \n")
        logging.error("O processamento falhou para a fila de arquivos, talvez tenha esquecido da entrada/saida ou os diretórios já estão populados")
  
    main()

def clean_dir(img_dir):
    arquivos = glob.glob(f"{img_dir}/*")
    try:
        for arquivo in arquivos:
            if os.path.isdir(arquivo):
                shutil.rmtree(arquivo)
            if os.path.isfile(arquivo):
                os.remove(arquivo)
        logging.info("O processo de limpeza executou corretamente")
    except Exception as e:
        print(f"Falha ao limpar {arquivo}. Razão: {e}")
        logging.error(f"A limpeza do diretório falhou. Razão: {e}")
    
    main()

def main():
    print("Digite E para extração de imagens do pdf, L para a limpeza do diretório de output e X para suspender o script")
    escolha = input().lower()
    if escolha == 'E'.lower():
        extract_image(workdir, output)
    elif escolha == 'L'.lower():
        clean_dir(output)
    elif escolha == 'X'.lower():
        sys.exit()
    else:
        main()          

if __name__ == "__main__":
    main()
