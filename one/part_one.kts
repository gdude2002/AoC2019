import java.io.File
import kotlin.math.floor

fun getFuel(mass: Float) : Float {
    return floor(mass / 3) - 2
}

fun getTotal() : Float {
    var total = 0f

    File("data.txt").forEachLine {
        total += getFuel(it.toFloat())
    }

    return total
}

fun main() {
    print("Total mass: ${getTotal().toInt()}")
}

main()
