def minutos_segundos(min):
    formula = min * 60
    return f"El resultado es {formula}"

def horas_minutos(hr):
    formula = hr * 60
    return f"El resultado es {formula}"

if __name__ == '__main__':
  min = 2
  hr = 2
  print(minutos_segundos(min))
  print(horas_minutos(hr))
