from pydub import AudioSegment

#audio = AudioSegment.from_mp3(r"D:\Robotica\Python Programacion Juegos USB\Proyectos Python-Arduino\Metegol\Goles-Arg\GolArg2-mp3.mp3")
audio = AudioSegment.from_mp3(r"D:\Robotica\Python Programacion Juegos USB\Proyectos Python-Arduino\Metegol\Anuncios\Anuncio6-mp3.mp3")


#audio.export(r"D:\Robotica\Z-Musica Sonido Juegos\.wav", format="wav")
#audio.export(r"D:\Robotica\Python\Reprod sound aleat de una lista\Sonid-wav-Ganador.wav", format="wav")
#audio.export(r"D:\Robotica\Python Programacion Juegos USB\Proyectos Python-Arduino\Metegol\Goles-Arg\GolArg2-wav.wav", format="wav")
audio.export(r"D:\Robotica\Python Programacion Juegos USB\Proyectos Python-Arduino\Metegol\Anuncios\Anuncio6-wav.wav", format="wav")