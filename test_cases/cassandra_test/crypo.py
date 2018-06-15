#!/usr/bin/env python3

from Crypto.Cipher import AES
# Encryption
encryption_suite = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
cipher_text = encryption_suite.encrypt("A really secret message. Not for prvying eye  s.")
print(cipher_text)
# Decryption
cipher_text=b'0x8cb8f805fcd37b7a299a1df3ba9b56eb53a39b6b24d2ecba9a89396ec8a3591f189203aba5bf35b1edcb7c1a0e9a1c5627706158cd70f8dd64f9933b407a37b6340d8d598b9c4143bf7b44a47a4bf69189ba026d2d67853820be754b7c9a9e14e2fda2fc06785509b54a70949ef2e5704152a9c56325cbb382098633ded389e53d2ea3766a4de1f9328ca27809723227de1c3e9ce13658ff07a09dae333e35cced0f9222885fc4ebece728bc814a33af4739303150800d790e18f32cb0831c9acb4ad8073b076858d614250b0f00fb388a72b9e62741fdc10c7c4676fa39924ecb574d2915841ea9c126ab54845940ed50a3678cef4722bcd3d301f43ba8f7be608971a45b808b6a7812f928954fc0704835e5cdfa650939121016cc4f1680c5555be94b7e75a9e2d588d82fb9a4f8566fda8999da24a872e6a5e82e63d27a368f0a122f490438afb8c5137885ae8151ff70e6ba6f3501f09193f452b560052f56a49998b913f49ef4f3659a32fcedd2041c361a4b876754018ce4af156a84ccbbd4659b66be065a84c718cd5da39e414ff8604be6f97d8d681fe8a41378c118ca472137883f2b691d03dcefca646a7edf36cd1ba380d17c10b3e4d08802882b23efa0c1df5119df0c90e68f9496d9cdbdeff97be8aae1b98c01e9fc8e2f95cfa9eae0e3af5c4222b29ab2136b4be4526504fe0add26358430c7d1a304770b68e43861380761a5426c8e7983430a5aa67f374f25085f19c9a48fdf3ec26485bdda730e306f6abdf3faf093a640674c0badf4cc36db893b77a8ec380a6fb5b27cb72d5d95f3ae27f0610a146268c1f6a77eeeea349d4368f1694c767c92f0feb7afb57f15ab2f0947e9aebbe6b8601bf5ac194317178f0fb9ee2c76269dada9b9ce14c56d4a461c3bc2531409d458bfd71a5f61d5f35658d5dba04382f515fb6bf8c55f4103c5cfcf49824a9002bf69fa62c4b3468761af1cd5bf93aca266ad816c4773055d579badd2b1ecf2bb71cd9b90019d5279b81fdeafc923d34a4bd1d673c858f0e8055e389af851b67bdfa566df901cb1581ae7051d354d291f733beb39c8adc848aa0618b2d6cf43a19a01b2991136d32b5a7b958eaa85da31f49ce49d2cb4951cb582d203182e0ce01f2833b797bbd6f58d82634c62089e207517f7baf417205b568128ec1dfaa484ca16a15776e30d9fa06498fa833d6f155e2f57d5234526f452b93523e12477f21e746d525375db7a07886dbded6f60d6eefd3b97368453ae2ad1296bbeaf3e43af58462bb342e0b8e091d230ed253ff2c69fbdf2e95145398c5d63976831423c9a0b1fb36208db76e877b85c2ef782c5c917c52e9bcb3d64c90ddef96c30cceb511306493bf22c3b0594b58b344a291da08fe285974bfcc77e577b640ee3719d2829d8fa3a4ba942797c4cc96dcdd6ada08a5d'
decryption_suite = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
plain_text = decryption_suite.decrypt(cipher_text)
print(plain_text)