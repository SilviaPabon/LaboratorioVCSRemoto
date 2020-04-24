object informe11L extends App {
  import scala.util.Random

  //Se crea un una función llamada generador que por medio de dos ciclos for retorna un arreglo bidimensional con numeros psuedoaleatorios
  def generador(mini:Int,maxi:Int):Array[Array[Int]] = {
    val arr = Array.ofDim[Int](4,12)
    for (i <- 0 to 3) {
      for (x <- 0 to 11) {
        arr(i)(x) = mini + Random.nextInt( (maxi+1) - mini )
      }
    }
    return arr
  }

  //La función imprimir, imprime un arreglo bidimensional en forma de una tabla con ciudades y meses. Utiliza ciclo for y condicionales para crear los espacios entre los datos
  def imprimir(arr:Array[Array[Int]]):Unit = {
    val meses = Array("ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic")
    val ciudad = Array("  Bucaramanga", "Floridablanca", "        Girón", "  Piedecuesta")
    var mes = ""
    for (i <- 0 to 11) {
      mes =  mes + meses(i) + "   "
    }
    println("               " + mes)

    for (i <- 0 to 3) {
      var espaciado = ""
      for (j <- 0 to 11) {
        espaciado = espaciado + (arr(i)(j))

        if ((arr(i)(j) >= 100) || (arr(i)(j) <= -10)) {
          espaciado += "   "
        }else if ((arr(i)(j) >= 10) || ((arr(i)(j) >= -10) && (arr(i)(j) < 0))) {
          espaciado += "    "
        } else {
          espaciado += "     "
        }
      }
      println(ciudad(i) + "  " + espaciado)
    }
    print("\n")
  }

  //La función restador resta dos arreglos bidimensionales, mediante dos ciclos for.
  def restador(A:Array[Array[Int]],B:Array[Array[Int]]):Array[Array[Int]] = {
    var R = Array.ofDim[Int](4,12)
    for (i <- 0 to 3) {
      for (x <- 0 to 11) {
        R(i)(x) = A(i)(x) - B(i)(x)
      }
    }
    return R
  }

  //La función generador3D retorna dos arreglos tridimensionales teniendo como entrada dos arreglos bidimensionales. Se utiliza ciclos para obtener los arreglos tridimensionales.
  def generador3D(ingresos:Array[Array[Int]],egresos:Array[Array[Int]]):(Array[Array[Array[Int]]],Array[Array[Array[Int]]]) = {
    var ingresos3D = Array.ofDim[Int](5,4,12)
    var egresos3D = Array.ofDim[Int](5,4,12)
    for (i <- 0 to 3) {
      for(x<- 0 to 11) {
        ingresos3D(0)(i)(x) = ingresos(i)(x)
        egresos3D(0)(i)(x) = egresos(i)(x)
      }
    }

    for (i <- 1 to 4) {
      for (x <- 0 to 3) {
        for (j <- 0 to 11) {
          ingresos3D(i)(x)(j) = ((ingresos(x)(j))/ 1.095).toInt
          ingresos(x)(j) = ingresos3D(i)(x)(j)
          egresos3D(i)(x)(j) = ((egresos(x)(j))/ 1.056).toInt
          egresos(x)(j) = egresos3D(i)(x)(j)
        }
      }
    }


    return(ingresos3D , egresos3D)
  }

  //La función Imprimir3D imprime un arreglo tridimensional en formato de tabla para hacerlo más comprensible al usuario
  def imprimir3D(arr: Array[Array[Array[Int]]]):Unit = {
    val meses = Array("ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic")
    val ciudad = Array("  Bucaramanga", "Floridablanca", "        Girón", "  Piedecuesta")
    var mes = ""
    val años = Array("2019", "2018", "2017", "2016", "2015")
    for (i <- 0 to 11) {
      mes =  mes + meses(i) + "   "
    }
    val mes2 = Array(mes, mes, mes, mes, mes)

    for (x <- 0 to 4) {
      println("                                        " + "Año " + años(x) + "\n" + "               " + mes2(x))
      for (i <- 0 to 3) {
        var espaciado = ""
        for (j <- 0 to 11) {
          espaciado = espaciado + (arr(x)(i)(j))

          if ((arr(x)(i)(j) >= 100) || (arr(x)(i)(j) <= -10)) {
            espaciado += "   "
          }else if ((arr(x)(i)(j) >= 10) || ((arr(x)(i)(j) >= -10) && (arr(x)(i)(j) < 0))) {
            espaciado += "    "
          } else {
            espaciado += "     "
          }
        }
        println(ciudad(i) + "  " + espaciado)
      }
      print("\n")
    }
  }

  //La función calcular_ganancias3D calcula la resta de dos arreglos tridimensionales, obteniendo un arreglo tridimensional de salida. Se utilizan ciclos para este fin.
  def calcular_ganancias3D(ingresos:Array[Array[Array[Int]]], egresos:Array[Array[Array[Int]]]):Array[Array[Array[Int]]] = {
    var ganancias3D = Array.ofDim[Int](5,4,12)
    for (i <- 0 to 4) {
      for (x <- 0 to 3) {
        for (j <- 0 to 11) {
          ganancias3D(i)(x)(j) = ingresos(i)(x)(j) - egresos(i)(x)(j)
        }
      }
    }
    return ganancias3D
  }


  // ------------------------------------Principal -------------------------//
  val ingresos = generador(100,180)
  val egresos = generador(60,130)
  val ganancias = restador(ingresos, egresos)

  imprimir(ingresos)
  imprimir(egresos)
  imprimir(ganancias)

  val arr3D = generador3D(ingresos,egresos)
  val ingresos3D = arr3D._1
  val egresos3D = arr3D._2
  val ganancias3D = calcular_ganancias3D(ingresos3D,egresos3D)


  imprimir3D(ingresos3D)
  imprimir3D(egresos3D)
  imprimir3D(ganancias3D)


}
