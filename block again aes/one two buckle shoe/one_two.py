##############################################################################################
### HELPER FUNCTIONS

def arrangeInMs(str):
    # Split the string into bytes
    bytes_list = str.split()
    # Group the bytes into chunks of 10
    chunks = [bytes_list[i:i + 16] for i in range(0, len(bytes_list), 16)]
    # Join each group of 10 bytes into a string and store in the final list
    list_of_chunks = [' '.join(chunk) for chunk in chunks]
    # Output the list
    return list_of_chunks

def xorHexStrings(stra, strb):
    # Remove spaces and convert to integers
    inta = int(stra.replace(" ", ""), 16)
    intb = int(strb.replace(" ", ""), 16)

    # XOR the integers
    result_int = inta ^ intb

    # Convert the result back to hex, removing the '0x' prefix and making it uppercase
    return format(result_int, 'x').upper()

def toAscii(str):
    return bytes.fromhex(str).decode('ascii')

###################################################################################################

version_1_str =  "99 02 A6 5C 25 96 EF 26 53 25 97 21 A2 6D E3 89 82 7B 33 0F D8 C6 B0 D8 21 74 B1 1B F9 41 CD 3E 3A 30 83 8F 5A 15 21 E0 61 95 FC 39 3D 06 8B 26 67 97 74 D5 B1 59 F5 BF 96 EC CC E2 DB 11 A2 60 23 24 4E 41 98 6E 8C 94 F5 E4 52 61 31 83 BE C3 ED 8B BF 32 F0 E9 F4 60 13 12 EA 70 30 1F 80 C0 DD 6A 24 CE AF BF B8 B8 92 95 7C 1D 7C E4 63 C2 40 AF D9 B6 EF 69 52 4F E4 92 61 38 20 C0 FC 26 35 9C 82 30 0C 60 1E 07 3E F5 D4 34 37 6C EE F7 57 D3 82 E3 B3 16 43 E4 26 84 54 F3 FE C3 49 2B 30 3D FC A6 86 88 4B 43 9F 0E 82 DE 58 A7 9D 09 F2 A5 5B 84 C1 B5 73 AF BF 67 5D 06 EC 5C 66 5B B7 BF 4D 6F 8E FA E4 24 FC 1B CF 19 41 72 B4 91 84 86 54 56 DF A7 59 8C 13 D9 E7 87 92 72 8E 3F 45 A2 28 26 1C 2C 00 20 18 2D EA 5A 6A 5B F8 A3 E3 D3 4B 60 62 09 BB D2 8D BC F3 79 9D 25 83 AF B8 03 EA 01 56 5E 7F 57 2F B1 C3 42 C0 EA 28 30 51 DA F3 38 F2 43 D9 F2 B1 53 23 8C 1A 79 C8 66 7E 05 91 84 63 54 BF 02 3F 88 C9 E0 D7 AC 3B AB E2 E0 B4 9B 84 D8 E7 5C 07 C0 D5 E5 BB A8 58 11 20 55 A1 40 3B 5C F2 DA A1 A3 DA FA F4 0F 54 71 52 FA C2 68 74 75 97 99 A8 F6 B8 BE 21 0D CC DA D3 F4 A4 5C BA 2D F8 07 FA 8D F5 EB 98 33 3B 2C 7B A2 32 D5 7D E5 1A E9 80 2E D1 33 D2 ED A7 DB 7E 47 78 D2 80 74 6B F6 AB D8 55 CD 7C 29 A7 2A 46 14 CF A3 21 49 2E FD 1B 67 BA A1 8B 2D 78 A6 6A 7F A0 20 CC BF F8 76 25 88 1D 92 50 E6 93 5E 7F 5C 95 BE A0 7B 0E FF 4B 8D 4C F6 B3 01 FB C3 B0 FB F5 91 E6 09 A8 C4 CF 28 52 15 94 A1 47 16 6E 84 74 4D 44 6F 61 DF 2C 0B 35 FD E4 3A C6 57 DD A0 59 01 15 7D 8D F0 41 81 49 94 B3 FD 97 E2 0F 5B D6 E5 51 74 D1 42 9C 27 4E EF F4 A5 67 51 D8 1F A6 57 CF 48 EC 36 5F A7 0D DB 3B F3 12 BB DE 32 67 7B F9 CC 23 5D 5F AB 3B 20 B0 B6 0D 3D F7 2F E3 99 10 89 F2 6F CC 19 FB D4 E7 ED 98 A3 0A 66 BD 72 42 9F 41 23 EE F3 CF A4 05 28 F1 7D 0B BD FD B0 10 59 26 56 DB B0 CC 6E E4 60 FE 76 18 D4 1A 6C 9E 18 F0 A0 63 5F A8 97 AB E1 DB 07 07 69 0B DF 3F E8 2E EA FD A9 8E 6F 61 01 CA CA DC B8 5F FC 50 F2 29 3B 82 4A 2A 70 B3 4D 9E E8 03 1F 44 5D 90 7B A3 48 BF 50 56 10 1F CB C7 CF 7A C7 48 6B 7F 16 65 F8 F6 01 72 35 AB FB D1 6A BF D2 A8 B9 6A 2F 7C D7 50 81 3B 96 61 9C 4D 7F E9 0A F8 E8 B4 2D C4 31 FF 63 B3 10 01 C7 B0 E4 78 C1 5F 5D C0 48 2B 03 47 40 60 2A 45 D2 0D BF 03 17 E2 1D 84 A4 32 00 57 C3 A3 EE 81 25 CB C9 1B B4 58 38 C5 9C 67 F6 21 04 CA 11 A9 FB 46 FD 97 B5 EF 65 C6 0E CD EC 6B A3 75 89 6D AD 54 3E 1B 36 88 FD 27 03 A4 14 C4 ED A8 BA 08 93 13 B7 96 A0 77 7E 0E 56 2C A6 5B C2 25 84 4A CE DA C0 B3 F5 9D BA 7E 31 77 92 E8 C1 75 E2 D1 14 71 0D 47 9E 93 3F D4 CF 0E DE 6E 46 B7 89 A1 48 62 9D B7 DF A1 53 8B 53 8B 23 0B 91 B0 5C 19 5F B4 00 8C 5A 43 2C DC FD D7 EE 8C 42 1D 3F 10 E2 A8 94 BE 18 FD EC 0D 77 C7 43 0E 51 3C 66 BF AF 9A 28 D9 A7 E5 30 40 81 17 9C 08 F5 FD 26 81 AA 8E BF D4 FD F5 99 4D F7 61 92 E8 57 BA 05 BC 7C F4 A9 2A BD C0 63 DF 54 43 C6 9F 0A FF 3F F4 21 5D 2A 21 43 7A D4 96 D1 76 9C 31 CE 6F 71 70 F4 5C D0 92 88 F3 D5 1B E1 27 FA FB A6 0C 58 80 74 80 F8 8F 79 25 A2 B7 E3 EE 29 A4 D4 95 3E 58 E5 A5 3F 88 08 EC 8B 44 01 35 C3 B4 28 54 69 89 29 5B 1D 60 C3 F5 FD 90 E2 58 22 97 AB 53 60 17 C8 33 81 9F 36 3D C9 D0 61 F7 D5 67 82 33 71 56 12 87 33 F0 3C 97 56 D3 4D 43 E8 22 87 F0 51 6E 97 27 92 96 2C 63 2D 47 91 38 E6 AB B4 E7 CF 44 2F 5D 79 95 0F 8B 3F 59 EF 5C 06 F9 CA 72 9E AA E1 1C B6 A5 B5 B7 10 5C 8A C0 5C EB 2A 5D 6F 36 1B 8B 1A F2 86 97 C7 49 BC E5 9B 0D 54 27 CF F8 FE 31 24 57 5B EB B7 8F 38 B7 FE FC 23 78 54 EB 21 B1 3D E4 85 94 5C 36 10 2D 33 42 89 4A 5F 7C EA 72 B4 2A 30 69 AE 41 42 3D 06 A1 7A 55 96 B8 0E 4F 0D BE 58 38 86 1F 0D 05 51 E7 9B CE 94 9D 46 A7 D1 A8 6D 53 4B 57 3C C2 3B 45 CA 9D D0 C6 E3 1D 32"
version_11_str = "99 02 A6 5C 25 96 EF 26 53 25 97 21 A2 6D E3 89 82 7B 33 0F D8 C6 B0 D8 21 74 B1 1B F9 41 CD 3E 3A 30 83 8F 5A 15 21 E0 61 95 FC 39 3D 06 8B 26 67 97 74 D5 B1 59 F5 BF 96 EC CC E2 DB 11 A2 60 23 24 4E 41 98 6E 8C 94 F5 E4 52 61 31 83 BE C3 ED 8B BF 32 F0 E9 F4 60 13 12 EA 70 30 1F 80 C0 DD 6A 24 CE AF BF B8 B8 92 95 7C 1D 7C E4 63 C2 40 AF D9 B6 EF 69 52 4F E4 92 61 38 20 C0 FC 26 56 CE DB 43 55 13 1E 6B 7F B7 D8 34 55 39 AA B6 64 C4 88 C4 C0 4F 37 C0 22 C6 14 B2 DE D9 5F 2B 34 37 FD AB AC F5 7E 58 DA 47 80 C9 55 A4 99 0D E2 EA 40 93 C1 B6 7A B9 BF 68 5C 02 E6 5E 63 57 B0 BF 45 6F CF E2 F5 32 B5 0E 80 04 42 3C B4 9D 91 C3 47 59 D2 EB 48 96 1D C2 EA 98 86 3D 9B 33 5F A2 7A 33 11 7E 0F 2C 0B 20 A3 0A 79 40 EA AB EC DD 18 3A 58 4F 81 BD F3 90 F9 79 B3 32 83 A1 B9 0D EB 0F 3F 5A 13 6C 09 D8 EE 10 F6 DA 25 0C 13 F3 E0 7A E0 17 81 B0 FE 1C 16 9B 11 4F D5 15 2A 21 95 C6 07 45 A7 04 7C 8A DE E9 D2 A8 2D EE AD D3 E4 E6 E0 DD E3 5B 54 D8 D1 ED EC BD 42 11 3B 6F FA 7C 77 55 F4 C1 A1 F6 D0 F8 F4 0F 54 71 52 DF D9 78 6D 2C 89 91 B7 A1 B6 AA 64 59 C5 D1 97 90 B0 5E EF 6C B5 14 F3 89 E1 F5 89 33 35 24 3F F6 3B C3 7D ED 54 ED 80 2E D0 36 C1 AC BC D4 31 5D 3C 97 C9 79 60 EE BA C2 47 CD 7E 2C F3 22 09 1E 91 EC 38 5D 2E E1 4F 68 B5 A4 8B 69 2F AE 3E 73 F2 2E D2 EF D0 57 25 DE 59 9A 54 BF C4 5C 6E 46 DB BA A2 7B 26 D4 1B D1 0E FB A6 58 B2 C6 A6 E0 FF 91 B1 72 FB E1 9F 25 53 18 C0 E7 47 16 7C 81 7C 51 5F 46 32 EE 69 0B 28 FC A0 7C CE 57 9C A2 50 0F 15 60 98 F9 4A CD 49 9E A2 AF 95 E9 0F 71 C6 E3 04 3B E5 42 86 6F 5E F4 EE A5 24 60 97 34 BF 4D D3 1C F3 64 76 E2 1A C0 74 E5 57 9B D4 3E 7F 30 D4 CD 09 1F 22 FF 3D 2E F3 B7 1B 69 F3 22 F3 99 26 89 ED 74 85 03 EE 95 C0 FD 9A F6 4B 61 B7 21 44 8B 41 2E E2 EE 86 8E 4B 14 EE 28 66 B5 EA E3 56 08 79 07 92 E3 96 0C 8B 09 FD 37 39 C2 02 3E C9 08 A0 FC 2E 13 A5 8C A7 B2 96 12 0E 7F 07 8D 3B BC 6F C7 EE BC A4 65 5B 52 A6 DF DB F9 42 BD 43 F2 60 1B 99 43 18 7D 85 09 F2 E0 0F 1F 55 52 C2 66 A4 5F B3 52 59 05 0E C6 88 C8 75 8B 09 66 30 13 67 ED F1 1C 6E 35 AB FB D1 6A FE DF E1 B7 6C 2D 77 96 53 9A 69 83 7D 90 02 70 A7 0A FD FC AE 2A D0 31 F1 71 B3 05 07 82 F1 F6 36 D9 56 50 93 54 36 48 46 49 37 25 0B 9F 0D A0 54 0F F5 0C 88 F1 2B 03 50 CF BC A0 D5 20 CF DC 4C B6 4B 31 85 9C 63 D5 31 30 EB 41 B8 E1 0D A4 F6 A2 AE 7D C2 4B 9E D4 73 99 59 D9 7C B6 17 7B 7A 09 C9 FA 3F 03 F6 14 CE F9 ED D6 1D 98 5E B3 D8 8A 7A 74 04 56 3A F5 44 D3 60 E8 46 CD 96 D6 BC E6 94 E3 42 38 72 DF F9 F2 28 9F 9C 14 73 1E 06 A5 84 7E FC 83 21 D2 7F 74 E0 BA E0 45 2C BA D2 C4 87 12 CD 3E 84 0A 3A AA F6 69 41 6E B4 37 A1 6D 37 61 95 DC E1 C7 BB 75 14 22 45 DE E5 85 A4 53 FD CD 0D 6F D5 50 50 14 68 48 B6 BD 92 6D C6 E8 A9 0B 40 87 17 9D 04 A1 FC 3C 8A BC 8F BF D6 E9 ED CE 58 EA 24 83 AD 03 BB 1F B7 39 E3 E8 28 AD 9A 49 A1 7D 2F E5 BD 10 AB 16 D4 52 03 08 18 74 0B 93 C9 C4 6E 82 38 B1 19 75 67 F8 23 D6 EB 8F FF DD 11 F1 27 F7 E6 E9 50 52 A6 43 B7 CF 82 4D 18 86 84 D9 C9 12 84 FE EF 04 4E E1 A9 3E C0 0C E6 CA 4A 01 66 E9 B5 71 77 65 B8 65 7E 0F 6A 86 F8 B3 91 F7 0D 05 80 F2 74 71 21 C8 0F 81 8E 65 23 C8 C1 69 A2 D0 6C C3 2B 60 40 5B 84 72 EC 29 C0 4D C9 4C 43 C1 39 88 FB 49 6F 97 35 DC D9 03 10 09 03 D4 5D C2 BB B4 E4 CB 44 6A 1C 76 DB 22 F8 0E 55 BB 71 05 EE CB 63 9C B0 ED 74 A2 A5 B6 F6 03 15 9F C6 13 EA 20 4B 7D 2C 52 B7 16 BC 92 83 C7 56 B8 F2 9B 11 57 64 C9 EF E5 33 38 05 5B BE A4 9F 29 AB AC B3 31 30 42 AE 23 B2 3A FA 9F D7 5C 24 0D 27 2F 11 DD 4D 5C 7C EE 6F B3 66 12 6B A2 5C 45 21 03 AB 7A 7E BE CB 5A 46 1C EA 72 3A 80 58 38 47 0A C3 B1 80 D0 CF 66 C6 A5"

version_1 = arrangeInMs(version_1_str)
version_11 = arrangeInMs(version_11_str)

previous_m = '20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20'
message = ''

for i in range(8, len(version_11)):
    m_plus_m = xorHexStrings(version_1[i], version_11[i])
    decryption = xorHexStrings(m_plus_m, previous_m)
    previous_m = decryption  
    message += toAscii(decryption)

print(message)

    