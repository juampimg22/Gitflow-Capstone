import mas_retweets
import dias
import hashtags
import usuarios

def main(archivo):
    mas_retweets.mas_retweets(archivo)
    dias.dias(archivo)
    hashtags.hashtags(archivo)
    usuarios.usuarios(archivo)
    return 'Gitflow'
