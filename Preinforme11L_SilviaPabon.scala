object Preinforme11L extends App {
  //Ejemplos con arreglos bidimensionales y multidimensaionales, punto 1
  val rows = 2
  val columns = 2
  val array7 = Array.ofDim[Int](rows,columns)
  array7(0)(0) = 1
  array7(0)(1) = 2
  array7(1)(0) = 2
  array7(1)(1) = 5
  println(array7)

  var a: Float = 0
  var c: Float = 0
  for (i <- 0 to 1; j <- 0 to 1) {
    a += array7(i)(j)
    c += 1
    println(a/c)}

  val arr = Array.ofDim[Int](3,3,3)
  arr(0)(0)(0) = 1
  arr(0)(0)(1) = 2
  arr(0)(0)(2) = 3
  arr(0)(1)(0) = 7
  arr(0)(1)(1) = 8
  arr(0)(1)(2) = 9
  arr(0)(2)(0) = 21
  arr(0)(2)(1) = 23
  arr(0)(2)(2) = 24

  val d = arr(0)(0)(0)*arr(0)(1)(0)*arr(0)(2)(0)
  println(d)

  //Solución planteamiento parte A con Scala
  def clima():Array[Array[Array[Int]]] = {
    val arr = Array.ofDim[Int](3,3,3)
    arr(0)(0)(0) = 33
    arr(0)(0)(1) = 35
    arr(0)(0)(2) = 40
    arr(0)(1)(0) = 8
    arr(0)(1)(1) = 8
    arr(0)(1)(2) = 9
    arr(0)(2)(0) = 10
    arr(0)(2)(1) = 10
    arr(0)(2)(2) = 10
    arr(1)(0)(0) = 30
    arr(1)(0)(1) = 28
    arr(1)(0)(2) = 27
    arr(1)(1)(0) = 7
    arr(1)(1)(1) = 8
    arr(1)(1)(2) = 7
    arr(1)(2)(0) = 10
    arr(1)(2)(1) = 10
    arr(1)(2)(2) = 10
    arr(2)(0)(0) = 10
    arr(2)(0)(1) = 9
    arr(2)(0)(2) = 8
    arr(2)(1)(0) = 6
    arr(2)(1)(1) = 6
    arr(2)(1)(2) = 6
    arr(2)(2)(0) = 10
    arr(2)(2)(1) = 10
    arr(2)(2)(2) = 10
    return arr
  }

  def promTemp(Clima:Array[Array[Array[Int]]], fila:Int): Int = {
    var s = 0
    var s1 = 0
    for (i <- 0 to 2) {
      s = s + (Clima(fila)(0)(i))
    }
    val prom = s/3
    return prom
  }

  def humedadRelativa(Clima:Array[Array[Array[Int]]], fila:Int): Float = {
    var va = 0
    var vs = 0
    for (x <- 0 to 2) {
      va = va + Clima(fila)(1)(x)
      vs = vs + Clima(fila)(2)(x)
    }
    val va2 = ((va:Float)/3):Float
    val vs2 = ((vs:Float)/3):Float

    val humedad = (va2/vs2)*100
    return humedad
  }

  def puntoRocío(Clima:Array[Array[Array[Int]]], fila:Int): Double = {
    val temp = promTemp(Clima, fila)
    val humedad = humedadRelativa(Clima,fila)
    val a = (humedad/100):Float
    val b = ((1:Float)/(8:Float))
    val Pr = (math.pow(a,b)*(110+temp))-110
    return Pr
  }




  val Clima = clima()
  println("La temperatura promedio de Barrancabermeja es: " + promTemp(clima, 0))
  println("La temperatura promedio de Bucaramanga es: " + promTemp(clima, 1))
  println("La temperatura promedio de Bogotá es: " + promTemp(clima, 2))

  println("El promedio de la humedad relativa de Barrancabermeja es: " + humedadRelativa(clima, 0) + "%")
  println("El promedio de la humedad relativa de Bucaramanga es: " + humedadRelativa(clima, 1) + "%")
  println("El promedio de la humedad relativa de Bogotá es: " + humedadRelativa(clima, 2) + "%")

  println("El promedio del punto de rocío de Barrancabermeja es: " + puntoRocío(clima, 0))
  println("El promedio del punto de rocío de Bucaramanga es: "+ puntoRocío(clima, 1))
  println("El promedio del punto de rocío de Bogotá es: " + puntoRocío(clima, 2))

  }


