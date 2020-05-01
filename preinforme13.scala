

object preinforme13 extends App {

  //----Sol. Parte B. punto 1----//

  //La función studentScores imprime las llaves y valores del diccionario scores
  //También imprime el primer valor de la lista, de cada llave
  def studentScores(): Unit = {
    val scores = Map("Omar" -> List(5.0, 4.0),
      "Silvia" -> List(4.0, 4.0),
      "Juanito" -> List(1.0, 4.9))
      for (i <- scores) {
        println("Las notas de primer y segundo parcial del alumno: "+ i)
      }
    println("La nota del primer parcial de Omar es: " + (scores("Omar")(0)))
    println("La nota del primer parcial de Silvia es: " + (scores("Silvia")(0)))
    println("La nota del primer parcial de Juanito es: " + (scores("Juanito")(0)))
  }

  //----Sol. Parte B. punto 2----//

  //La función clima devuelve un diccionario donde cada llave es una ciudad y los valores dentro de ellas son una lista de listas.
  //Las listas representan la temperatura, vapor de agua y vapor de agua saturado, respectivamente.
  def climate():Map[String,List[List[Double]]] = {
    val clima = Map("Barrancabermeja"-> List(List(33.0,35.0,40.0), List(8.0,8.2,8.5), List(10.0,10.0,10.0)),
      "Bucaramanga" -> List(List(30.0,28.0,27.0), List(7.0,7.5,7.4),List(10.0,10.0,10.0)),
      "Bogotá" -> List(List(10.0,9.0,8.0), List(5.9,6.0,6.2),List (10.0,10.0,10.0)))
    return clima
  }

  //La función promTemp calcula el promedio de la temperatura.
  //Tiene como valores de entrada el diccionario y una llave
  //Se utiliza un ciclo for para calcular la suma de las temperaturas y luego se dividen entre la cantidad sumada.

  def promTemp(clima:Map[String,List[List[Double]]] , ciudad:String): Double = {
    var suma = 0.0
    val cant = clima(ciudad)(0).length
    for(i <- 0 to cant-1) {
      suma = suma + clima(ciudad)(0)(i)
    }
    val prom = (suma/cant)
    return prom
  }

  //La función humedadRelativa calcula la humedad relativa en las 3 ciudades.
  //Se realiza un for para calcular la sumatoria del vapor de agua(va) y el vapor de agua saturado(vs), para después dividirlo entre la cantiddad de datos sumados y así obtener el promedio de ambos.
  //Por ultimo, se calcula la humedad relativa mediante la formula (va/vs)*100
  def humedadRelativa(clima:Map[String,List[List[Double]]], ciudad: String): Double = {
    var va = 0.0
    var vs = 0.0
    val cantVa = clima(ciudad)(1).length
    val cantVs = clima(ciudad)(2).length
    for (i<- 0 to cantVa-1){
      va += clima(ciudad)(1)(i)
    }
    for (i <- 0 to cantVs-1){
      vs += clima(ciudad)(2)(i)
    }
    va = va/cantVa
    vs = vs/cantVs

    val humedad = ((va/vs)*100)
    return humedad
  }

  //La función puntoRocío calcula la media del punto de Rocío de cada ciudad
  //Se utilizan las funciones anteriorres para obtener la temperatura y la humedad relativa y posteriormente se aplica la fórmula ((math.pow((HR/100),(1.0/8)))*(110+temp)-110)
  //Se utiliza la librería math para calcular la potencia
  def puntoRocio(clima:Map[String,List[List[Double]]], ciudad:String): Double = {
    val temp = promTemp(clima, ciudad)
    val HR = humedadRelativa(clima, ciudad)
    val Pr = ((math.pow((HR/100),(1.0/8)))*(110+temp)-110)
    return Pr
  }

  //----------------------------Principal---------------------------------//
  //----Sol. Parte B. punto 1----//
  studentScores()
  print("\n")

  //----Sol. Parte B. punto 2----//
  val clima = climate()

  println("El promedio de temperatura en Barrancabermeja es: " + promTemp(clima, "Barrancabermeja"))
  println("El promedio de temperatura en Bucaramanga es: " + promTemp(clima, "Bucaramanga"))
  println("El promedio de temperatura en Bogotá es: " + promTemp(clima, "Bogotá"))
  print("\n")

  println("El promedio de la humedad relativa de Barrancabermeja es: " + humedadRelativa(clima, "Barrancabermeja") + "%")
  println("El promedio de la humedad relativa de Bucaramanga es: " + humedadRelativa(clima, "Bucaramanga") + "%")
  println("El promedio de la humedad relativa de Bogotá es: " + humedadRelativa(clima, "Bogotá") + "%")
  print("\n")

  println("El promedio del punto de rocío de Barrancabermeja es: " + puntoRocio(clima, "Barrancabermeja"))
  println("El promedio del punto de rocío de Bucaramanga es: " + puntoRocio(clima, "Bucaramanga"))
  println("El promedio del punto de rocío de Bogotá es: " + puntoRocio(clima, "Bogotá"))
}
