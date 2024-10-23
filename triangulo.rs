use std::io::{self, Write};

fn verificar_semelhanca_lal(triangulo1: (f64, f64, f64), triangulo2: (f64, f64, f64)) -> bool {
    let (lado1_1, angulo_1, lado1_2) = triangulo1;
    let (lado2_1, angulo_2, lado2_2) = triangulo2;

    // Verifica se os lados são proporcionais e o ângulo entre eles é congruente
    (lado1_1 / lado2_1 == lado1_2 / lado2_2) && (angulo_1 == angulo_2)
}

fn verificar_semelhanca_aa(triangulo1: (f64, f64), triangulo2: (f64, f64)) -> bool {
    let (angulo1_1, angulo1_2) = triangulo1;
    let (angulo2_1, angulo2_2) = triangulo2;

    // Verifica se dois ângulos são congruentes
    (angulo1_1 == angulo2_1 && angulo1_2 == angulo2_2) || (angulo1_1 == angulo2_2 && angulo1_2 == angulo2_1)
}

fn verificar_semelhanca_lll(triangulo1: (f64, f64, f64), triangulo2: (f64, f64, f64)) -> bool {
    let (lado1_1, lado1_2, lado1_3) = triangulo1;
    let (lado2_1, lado2_2, lado2_3) = triangulo2;

    // Verifica se todos os lados são proporcionais
    lado1_1 / lado2_1 == lado1_2 / lado2_2 && lado1_2 / lado2_2 == lado1_3 / lado2_3
}

fn obter_triangulo(criterio: &str) -> Option<(f64, f64, f64)> {
    let mut input = String::new();

    if criterio == "LAL" {
        print!("Digite o valor do primeiro lado do triângulo: ");
        io::stdout().flush().unwrap();
        io::stdin().read_line(&mut input).unwrap();
        let lado1: f64 = input.trim().parse().unwrap();

        input.clear();
        print!("Digite o valor do ângulo entre os lados: ");
        io::stdout().flush().unwrap();
        io::stdin().read_line(&mut input).unwrap();
        let angulo: f64 = input.trim().parse().unwrap();

        input.clear();
        print!("Digite o valor do segundo lado do triângulo: ");
        io::stdout().flush().unwrap();
        io::stdin().read_line(&mut input).unwrap();
        let lado2: f64 = input.trim().parse().unwrap();

        Some((lado1, angulo, lado2))
    } else if criterio == "AA" {
        input.clear();
        print!("Digite o valor do primeiro ângulo do triângulo: ");
        io::stdout().flush().unwrap();
        io::stdin().read_line(&mut input).unwrap();
        let angulo1: f64 = input.trim().parse().unwrap();

        input.clear();
        print!("Digite o valor do segundo ângulo do triângulo: ");
        io::stdout().flush().unwrap();
        io::stdin().read_line(&mut input).unwrap();
        let angulo2: f64 = input.trim().parse().unwrap();

        Some((angulo1, angulo2, 0.0))
    } else if criterio == "LLL" {
        input.clear();
        print!("Digite o valor do primeiro lado do triângulo: ");
        io::stdout().flush().unwrap();
        io::stdin().read_line(&mut input).unwrap();
        let lado1: f64 = input.trim().parse().unwrap();

        input.clear();
        print!("Digite o valor do segundo lado do triângulo: ");
        io::stdout().flush().unwrap();
        io::stdin().read_line(&mut input).unwrap();
        let lado2: f64 = input.trim().parse().unwrap();

        input.clear();
        print!("Digite o valor do terceiro lado do triângulo: ");
        io::stdout().flush().unwrap();
        io::stdin().read_line(&mut input).unwrap();
        let lado3: f64 = input.trim().parse().unwrap();

        Some((lado1, lado2, lado3))
    } else {
        None
    }
}

fn verificar_semelhanca(triangulo1: (f64, f64, f64), triangulo2: (f64, f64, f64), criterio: &str) -> bool {
    match criterio {
        "LAL" => verificar_semelhanca_lal(triangulo1, triangulo2),
        "AA" => verificar_semelhanca_aa((triangulo1.0, triangulo1.1), (triangulo2.0, triangulo2.1)),
        "LLL" => verificar_semelhanca_lll(triangulo1, triangulo2),
        _ => {
            println!("Critério inválido.");
            false
        }
    }
}

fn main() {
    let mut criterio = String::new();
    print!("Escolha o critério de semelhança (LAL, AA, LLL): ");
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut criterio).unwrap();
    let criterio = criterio.trim().to_uppercase();

    println!("Digite os valores para o primeiro triângulo:");
    let triangulo1 = obter_triangulo(&criterio).unwrap();

    println!("Digite os valores para o segundo triângulo:");
    let triangulo2 = obter_triangulo(&criterio).unwrap();

    let resultado = verificar_semelhanca(triangulo1, triangulo2, &criterio);

    if resultado {
        println!("Os triângulos são semelhantes pelo critério {}.", criterio);
    } else {
        println!("Os triângulos não são semelhantes pelo critério {}.", criterio);
    }
}
