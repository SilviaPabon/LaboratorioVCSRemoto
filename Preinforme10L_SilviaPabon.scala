

object Preinforme10 {
  def utilOperAn(): Array[Int] = {        
      var Uom = Array(27834, 23789, 30189, 30967, 32501, 32701, 31665, 17155, 4614, 834)
    return Uom
    }    
  //Array con las utilidades operacionales de Kellogg's entre los años 2008 a 2017
  
  def difer_promedios(Uopm: Array[Int]): Int = {
    val long = Uopm.length
    val sum1 = Uopm(long-1)+Uopm(long-2)/2
    val sum2 = Uopm(8)+Uopm(9)/2
    val difPro = sum1 - sum2
    return difPro
    }                                              
 
  // Función que cálcula la diferencia entre el año de mayor utilidad con el de menor utilidad. Se cálcula la mayor utilidad y menor utilidad utilizando un for y un condicional if, que evalúa cada valor hasta finalmente dejar el mayor y el menor. Finalmente se resta el mayor menos el menor, siendo la variable dif2.   
 
  def diferencia_bajo_alto(Uopm : Array[Int]): Int = {
      val long = Uopm.length
      var utilMayor = Uopm(0)
      var utilMenor = Uopm(0)
      for (i <- 0 to long-1) {
              if (utilMayor < Uopm(i)) {
                      utilMayor = Uopm(i)
              }
              if (utilMenor > Uopm(i)) {
                      utilMenor = Uopm(i)
              }
      }
      val difMayMen = utilMayor - utilMenor
      return difMayMen
  }                                            
 
  // Función para calcular la mediana. Primero se ordena el Array de menor a mayor utilizando el método de ordenamiento burbuja para posteriormente calcular la mediana, siendo el valor que divide en dos partes iguales el Array.
 
  def mediana(Uopm : Array[Int]): Float = {
    val long = Uopm.length
    var orden = 0
    for (i <- 0 to long-1) {
        for (j <- 0 to long-2) {
            if (Uopm(j) > Uopm(j+1)) {
                orden = Uopm(j)
                Uopm(j)= Uopm(j+1)
                Uopm(j+1) = orden
            }
        }
    }
    val Half = long/2
    if (long%2==0) {
        var mediana = ((Uopm(Half)+Uopm(Half-1)):Float)/2
        return mediana
    } else {
        var mediana = Uopm(Half+1)
        return mediana
    }
  }
 
  //Función que cálcula la media mediante un for, sumando todos los valores del Array y posteriormente dividiéndolo entre el número de valores que contiene. Con el cálculo de la mediana de la función anterior, se cálcula la diferencia entre la mediana y la media.
 
  def media_uo(Uopm : Array[Int]): Unit = {
    val Mediana = mediana(Uopm)
    val long = Uopm.length
    var s = 0
    for (i <- 0 to long-1) {
      s += Uopm(i)
    }
    val prom = (s: Float)/long
    val difPromed = Mediana - prom
    println("La mediana es " + Mediana + " y el promedio es " + prom + "; la diferencia entre la mediana y la media es " + difPromed)
  }
 
  //Función que cálcula el porcentaje que aporta cada año a la utilidad operacional acumulada. Se cálcula la utilidad acumulada mediante un for, sumando cada uno de los valores en cada iteración. Por último, mediante una regla de 3 sencilla, se cálcula el porcentaje que cada año le aporta al acumulado.
 
  def porcentajeUo(Uopm : Array[Int]):Unit = {
    var s = 0
    var porc = (0: Float)
    val cant = Uopm.length
    for (i <- 0 to cant-1) {
      s += Uopm(i)
    }
    var a = 2007
    for (i <- 0 to cant-1) {
      porc = ((Uopm(i)*100):Float)/(s:Float)
      a += 1
      println("El porcentaje que aporta el año " + a + " al acumulado es " + porc + "%")
    }
  }
 
  //Función que cálcula el déficit del año 2017 comparado con el año anterior, es decir, 2016. Estos dos años son los últimos, por lo que simplemente se realiza un lenght para obtener el numero de elementos que contiene el Array y posteriormente restar los últimos dos.
 
  def deficitUo2017(Uopm : Array[Int]):Int = {
    val long = Uopm.length
    val deficit = Uopm(long-2) - Uopm(long-1)
    return deficit
  }
 
  //Función que cálcula el porcentaje de déficit de cada año, siendo negativo en caso de que no exista déficit. Para la cual se utiliza un ciclo for que mediante una regla de 3 sencilla calcule el porcentaje de cada año y lo imprima.
 
  def porcentajeDeficitAnual(Uopm : Array[Int]): Unit = {
    val long = Uopm.length
    var d = 0 : Float
    var defic = 0: Float
    var año = 2008
    for (i <- 0 to long-2) {
      d = Uopm(i) - Uopm(i+1)
      defic =  ((d*100)/Uopm(i)): Float
      año += 1
      println("El porcentaje de deficit para el año " + año + " es " + defic + "%")
    }
  }
 
  //---------------------------------------------------------------Resultados----------------------------------------------------------------//
 
  var Uopm = utilOperAn()           
  println("La diferencia del promedio de los ultimos años y los primeros años es: " + difer_promedios(Uopm))
    println("La diferencia entre las utilidades operaciones del año con mayor utilidad y el de menor utilidad es: " + diferencia_bajo_alto(Uopm))
    porcentajeUo(Uopm)
    println("El deficit del año 2017 con respecto al año anterior es de " + deficitUo2017(Uopm) + " millones de COP")
    porcentajeDeficitAnual(Uopm)
    println("La mediana es: " + mediana(Uopm))
    media_uo(Uopm)
}
