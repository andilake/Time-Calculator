def add_time(act, sumar, dia="None"):
  fecha = ''

  fechaactual = {'hora':int(act[:(act.find(':'))]),'minuto':int(act[(act.find(':')+1):(act.find(' '))]),'ampm':act[(act.find(' ')+1):]}
  fechasum = {'hora':int(sumar[:(sumar.find(':'))]),'minuto':int(sumar[(sumar.find(':')+1):])}
  fechafin = {'hora':0,'minuto':0,'ampm':''}

  diasnum = {1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday',7:'Sunday',0:'None'}
  diasnom = {v:k for k,v in diasnum.items()}
  diaactual = diasnom[dia.capitalize()]
  diafin = 0

  minutos=fechaactual['minuto']+fechasum['minuto']

  if fechaactual['ampm']=='AM':
      horas=int(minutos/60)+fechaactual['hora']+fechasum['hora']
  else:
      horas=int(minutos/60)+fechaactual['hora']+fechasum['hora']+12

  if horas%24 >= 12:
      fechafin['ampm']='PM'
  else:
      fechafin['ampm']='AM'

  if minutos%60 < 10:
      fechafin['minuto']=str('0')+str(minutos%60)
  else:
      fechafin['minuto']=str(minutos%60)

  if horas%12==0:
      fechafin['hora']=str(12)
  else:
      fechafin['hora']=str(horas%12)
  diafin = diaactual+int(horas/24)

  if diaactual == 0:
      if (diafin - diaactual) == 0:
          fecha = fechafin['hora']+':'+fechafin['minuto']+' '+fechafin['ampm']
      elif (diafin - diaactual) == 1:
          fecha = fechafin['hora']+':'+fechafin['minuto']+' '+fechafin['ampm']+' (next day)'
      else:
          fecha = fechafin['hora']+':'+fechafin['minuto']+' '+fechafin['ampm']+' ('+str(diafin-diaactual)+' days later)'
  else:
      if (diafin - diaactual) == 0:
          fecha = fechafin['hora']+':'+fechafin['minuto']+' '+fechafin['ampm']+', '+diasnum[diafin]
      elif (diafin - diaactual) == 1:
          fecha = fechafin['hora']+':'+fechafin['minuto']+' '+fechafin['ampm']+', '+diasnum[diafin]+' (next day)'
      else:
          fecha = fechafin['hora']+':'+fechafin['minuto']+' '+fechafin['ampm']+', '+diasnum[diafin%7]+' ('+str(diafin-diaactual)+' days later)'
  return fecha