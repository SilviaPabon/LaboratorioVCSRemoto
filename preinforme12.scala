object preinforme12 extends App {
  //Función que calcula la diferencia entre el mayor y el menor con la utilización de un for para hallar el valor mayor y menor de la lista

  def difMayorMenor(presion: List[Double]): Double = {
    var mayor = presion(0)
    var menor = presion(0)
    val cant = presion.length
    for (i <- 0 to cant-1) {
      if (mayor < presion(i)) {
        mayor = presion(i)
      }
      if (menor > presion(i)) {
        menor = presion(i)
      }
    }
    val dif = mayor - menor
    return dif
  }
  //La función media calcula el promedio de una lista. Utiliza un for para calcular la sumatoria de los elementos y luego los divide entre la cantidad sumada

  def media(lista:List[Double]):Double = {
    var suma = 0.0
    val cant = lista.length
    for (i <- 0 to cant-1) {
      suma = suma + lista(i)
    }
    val prom = suma/cant
    return prom
  }

  ///La función mediana calcula la mediana de una lista. Utiliza un ordenamiento burbuja, con ciclos y condicionales, para ordenar la lista de mayor a menor.
  //Después se identifica el número de elementos que contiene la lista, en caso de que sean par se saca el promedio de la mitad de sus elementos.
  //En caso de ser impar, se toma el numero que divide en partes iguales la lista.
  def mediana(lista: List[Double]):Double = {
    import scala.collection.mutable
    val cant = lista.length
    var listaMutable = scala.collection.mutable.ListBuffer[Double]()
    for (i <- 0 to cant-1) {
      listaMutable += lista(i)
    }
    var orden = 0.0
    for (j <- 0 to cant-1) {
      for (i <-  0 to cant-2) {
        if (listaMutable(i)>listaMutable(i+1)) {
          orden = listaMutable(i)
          listaMutable(i) = listaMutable(i+1)
          listaMutable(i+1) = orden
        }
      }
    }
    var mediana = 0.0
    val mitad = (cant/2).toInt
    if (mitad%2 == 0) {
      mediana = (listaMutable(mitad) + listaMutable(mitad-1))/2
    } else {
      mediana = (listaMutable(mitad+1))
    }
    return mediana
  }

  //La función lista de Listas calcula los valores de las semanas que superaron o estuvieron por debajo de la media anual. Almacenando cada los que superaron y los que no en una lista diferente; así como también estos se almacenan en una lista.
  def listadeListas(lista: List[Double]):List[scala.collection.mutable.ListBuffer[Double]] = {
    val prom = media(lista)
    import scala.collection.mutable
    var listadeListas = List(mutable.ListBuffer[Double](), mutable.ListBuffer[Double]())
    val cant = lista.length

    for (i <- 0 to cant-1) {
      if (lista(i) > prom) {
        listadeListas(0) += lista(i)
      } else {
        listadeListas(1) += lista(i)
      }
    }
    return listadeListas
  }

  //La función temperatura calcula la temperatura promedio semanal, teniendo en cuenta la formula de T = PV/nR
  def temperatura(presion: List[Double]):collection.mutable.ListBuffer[Double] = {
    var presionAtm = collection.mutable.ListBuffer[Double]()
    var atm = 0.0
    val cant = presion.length
    for (i <- 0 to cant-1) {
      atm = presion(i)*1000
      presionAtm += (atm)/101325
    }

    var temperatura = collection.mutable.ListBuffer[Double]()
    for (i <- 0 to cant-1) {
      temperatura += (presionAtm(i)*510)/(17.16*0.082)
    }

    return temperatura
  }

  //#La función desviación estándar calcula la desviación estándar de una lista, sumando todos los elementos mediante un for, a la par que se restan por el promedio y se potencian al cuadrado
  //Una vez hecho lo anterior, se divide la suma obtenida entre la cantidad de numeros sumados y se potencia en 1/2.
  def desviacionEstandar(lista: List[Double]):Double = {
    import scala.math
    val prom = media(lista)
    var suma = 0.0
    var x = 0.0
    var potencia = 0.0

    val cant = lista.length
    for (i <- 0 to cant-1) {
      x = (lista(i)-prom)
      potencia = math.pow(x, 2)
      suma = suma + potencia
    }
    val des = math.pow((suma/cant), 0.5)
    return des
  }

  //La función impresion imprime los valores de una lista de una manera más estética y comprensible
  def impresion(lista: List[Double]):Unit = {
    val cant = lista.length
    for (i <- 0 to cant-2) {
      print(" " + lista(i) +  ", ")
    }
    print(" " + lista(cant-1) +  ". ")
  }

  //---------------------------------Principal----------------------------------//

  val presion = List(110.06, 107.89, 108.45, 108.49, 109.03, 110.11, 109.87,
    119.38, 119.35, 116.34, 117.73, 120.01, 118.19, 119.53,
    117.09, 118.03, 118.65, 117.47, 117.49, 109.65, 110.44,
    110.51, 107.38, 109.26, 106.18, 109.36, 106.61, 105.16,
    110.11, 105.48, 108.37, 107.59, 108.91, 108.35, 109.57,
    122.56, 124.44, 125.97, 121.03, 121.22, 122.41, 122.15,
    124.52, 123.35, 125.76, 121.08, 122.29, 105.42, 110.67,
    107.73, 105.76, 107.85)

  print("La lista con los datos de presion promedio semanal es: ")
  impresion(presion)
  println("\n"+ "\n" + "La diferencia entre el mayor y menor es: " + difMayorMenor(presion) + "\n")

  println("La media de las presiones promedio es " + media(presion) + " y la mediana es: " + mediana(presion) + "\n")

  val listaPresionMedia = listadeListas(presion)
  val listamayor = listaPresionMedia(0).toList
  val listamenor = listaPresionMedia(1).toList

  print("Los valores que superan al promedio anual son: " )
  impresion(listamayor)
  print(" y los valores que están por debajo del promedio anual son ")
  impresion(listamenor)
  println("\n")

  val temperature = temperatura(presion)
  val temp = temperature.toList
  print("La temperatura promedio semanal es: ")
  impresion(temp)
  println("\n")

  println("La desviación estándar de la temperatura promedio semanal es: " + desviacionEstandar(temp) + "\n")
  val temperaturamedia = listadeListas(temp)
  val tempmediaMayor = temperaturamedia(0).toList
  val tempmediaMenor = temperaturamedia(1).toList

  print("Las temperaturas promedio que superan la media anual son: ")
  impresion(tempmediaMayor)
  print(" y las que estan por debajo son: ")
  impresion(tempmediaMenor)
  println("\n")

  println("La desviación estándar de las temperaturas superiores a la media es: " + desviacionEstandar(tempmediaMayor) + " y la desviación de los más bajos de la media es " + desviacionEstandar(tempmediaMenor) + "\n")

  val desMayorMenorTemp = List(desviacionEstandar(tempmediaMayor) , desviacionEstandar(tempmediaMenor))
  println("La media de la desviación estándar de la temperatura mayor y menor que el promedio es: " + media(desMayorMenorTemp))





  // PUNTO 1

  // Importación de paquetes para trabajar con listas mutables e inmutables
  import scala.collection.mutable.ListBuffer
  import scala.collection.immutable._

  //Creación de lista mutable de enteros, que se llena con el resultado de multiplicar por dos el número de cada vuelta


  def main(args: Array[String]) {
    val numbers = ListBuffer[Int]()
    for (i <- 0 to 10) {
      numbers.append(i * 2)
    }
    println(numbers)
  }

  //Creación de lista inmutable de enteros, para luego sumar sus valores interiores

  def main(args: Array[String]) {
    val numbers2: List[Int] = List(10, 20, 30, 40, 50)
    var suma = numbers2.sum
    println(suma/numbers2.length)
  }











}