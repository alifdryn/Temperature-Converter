def kelvin_to_celsius(kelvin):
    """
    Mengonversi suhu dari Kelvin ke Celsius.
    """
    celsius = kelvin - 273.15
    return celsius

def celsius_to_kelvin(celsius):
    """
    Mengonversi suhu dari Celsius ke Kelvin.
    """
    kelvin = celsius + 273.15
    return kelvin

def temperature_converter(suhu, unit):
    """
    Mengonversi suhu dari Celsius atau Kelvin ke Fahrenheit.
    """
    if unit == 'C':
        kelvin = celsius_to_kelvin(suhu)
    elif unit == 'K':
        kelvin = suhu
    else:
        raise ValueError("Unit harus 'C' atau 'K'")

    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return fahrenheit

def fahrenheit_converter(suhu, output_unit):
    """
    Mengonversi suhu dari Fahrenheit ke Celsius atau Kelvin.
    """
    celsius = (suhu - 32) * 5/9
    if output_unit == 'C':
        return celsius
    elif output_unit == 'K':
        return celsius_to_kelvin(celsius)
    else:
        raise ValueError("Output unit harus 'C' atau 'K'")

def main():
    # Input suhu dan satuan dari pengguna
    suhu_input = float(input("Masukkan suhu: "))
    satuan_input = input("Masukkan satuan suhu ('C' untuk Celsius, 'K' untuk Kelvin, 'F' untuk Fahrenheit): ").upper()

    # Konversi ke Fahrenheit, Celsius, dan Kelvin
    if satuan_input == 'F':
        suhu_fahrenheit = suhu_input
        suhu_celsius = fahrenheit_converter(suhu_fahrenheit, 'C')
        suhu_kelvin = fahrenheit_converter(suhu_fahrenheit, 'K')
    else:
        suhu_fahrenheit = temperature_converter(suhu_input, satuan_input)
        suhu_celsius = fahrenheit_converter(suhu_fahrenheit, 'C')
        suhu_kelvin = fahrenheit_converter(suhu_fahrenheit, 'K')

    # Menampilkan hasil konversi
    print("\nHasil Konversi:")
    print(f"{suhu_input} {satuan_input} = {suhu_fahrenheit:.2f} Fahrenheit")
    print(f"{suhu_input} {satuan_input} = {suhu_celsius:.2f} Celsius")
    print(f"{suhu_input} {satuan_input} = {suhu_kelvin:.2f} Kelvin")

if __name__ == "__main__":
    main()
