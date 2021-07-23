# Category: Web

## Oregano Cafe

### Part 0

Flag found in the robots.txt file

> robots.txt

```
# Part 0 Flag: NEWBIE{be3p_b00p_tH!s_siT3_was_pLaGiar!s3D_i_m34n_syNth3sized}

User-agent: *
Disallow: /starch.py
```

Flag: `{be3p_b00p_tH!s_siT3_was_pLaGiar!s3D_i_m34n_syNth3sized}`

### Part 1

Upon trying a password, the website gives an error as well as the expected hash (`a4ec243c744c8424fcb454f4cc4464246ca40484243cd454bcf41424fc048c04`). From the robots.txt file, we can see a file `starch.py`, which when viewed shows the implemented hash function.

Reverse engineer this function to find the password which can be put in.

There is more than one correct password, due to how the hashing function handles the last character of the password input.

Password: `lo2eme30m5f2e5h0o0440e3nom.pmn/5`  
Flag: `NEWBIE{wriTinG_y0uR_0wn_ha5#_fuNcTi0N_iSnT_th3_b3St_id3A!}`  
Script: TODO:

## SecBin

File uploader which has and endpoint that allows you to view the file... or any other path in the filesystem. So we can do some LFI (Local File Inclusion) and Directory Traversal exploits to leak some secure files... like `/etc/passwd`

URL: `https://secbin.ctf.unswsecurity.com/download?file=../../../../../../../../../../etc/passwd`  
Flag: `NEWBIE{1m491n3_54y1N9_1T5_uH4x0r4bL3}`

---

# Category: Binary

## no_code_attached

> Given ASLR/PIE protection and a lack of address leak, we know this is not a `ret2win` challenge.  

The vulnerable function in the binary file reads in a password string and returns (as `eax`) the contents at `ebp-0x10`. The main function compares this result to `0x4269` and calls the win function (`top_secret_admin_stuff`) if it matches.

We can exploit the input loop to override the contents at `ebp-0x10`

Flag: `NEWBIE{h4v1ng_th3_c0de_sur3_h3lp5}`  
Script: TODO:

---

# Category: Forensics

## whitespace

> MS PAINT OP

The flag is handwritten in a slightly different colour than the background. Use a magic wand selection tool / change the background colour.

Flag: `NEWBIE{it_flooded}`

## My Favourite HEXagon

View the image as hex to find the flag (or like, use `strings`), in a reversed format.

Flag: `NEWBIE{h0w_d1d_u_f1nd_me}`

## world emoji day

A bunch of images, a text file and a corrupted 'image' is provided in a zip file. Looking at the corrupted "image", it is actually a corrupted PDF file (given away by some metadata tags). Throw it into a PDF file fixer and we can view the flag

Flag: `NEWBIE{Em0j!5_4r3_Coo!}`

---

# Category: Crypto

## secsoc x csesoc

Potentially a substitution cipher, as the second and sixth segments could correspond to the "E" in "N<u>E</u>WBI<u>E</u>". However jokes it's just a binary ASCII encoding of the flag, whose dits are replaced with either `csesoc` or `secsoc`.

We can replace `csesoc` as `0` and `secsoc` as `1`, then decode the segments.

Flag: `NEWBIE{W3lC0m3_T0_th3_CtF}`  
Script: TODO:

## Askii

Pretty simple challenge, each segment in the provided file is just the ASCII symbol.  
The flag is embedded inside a chunk of lorem text, so just CTRL + F after decoding everything

Flag: `NEWBIE{Ascii_Rul3s_Th0ugh}`  
Script: TODO:

## Base64 Onion

The flag is encoded in base64 many times, just continually decode until we find the flag.

Flag: `NEWBIE{N0_hop3_Ju5t_4dd1ng_l4y3rs}`  
Script: TODO:

---

# Recon

## a rocket

An image of a US rocket is shown. A quick reverse image search as well as searching for "US Rocket" and checking its location reveals the location of Alabama

Flag: `NEWBIE{Alabama}`

---

# Misc

## zippity 2: electric boogaloo 

We need to SHA-512 a bunch of potential flags to find the flag whose hash begins with `146`

The file turns out to be `boogaloo-2042.txt`.

Flag: `NEWBIE{e#p4!8C_g%4-M!3&R_m%0$m#e?n@T!}`  
Script: TODO:

## The Mining Canary

The flag is split into multiple payloads.

* HTML Comment: `NEWBIE{F12`
* CSS Comment: `_Ctr1+sh1ft+I`
* Cookie: `_m0r3}`

Flag: `NEWBIE{F12_Ctr1+sh1ft+I_m0r3}`

## Plumbing Advice

> question highkey stolen from skylight...

There's a script tag in the source code that tries to source a script from a supposedly non-existent domain.  
Check for `TXT` records with `dig` to find it (i.e. `dig favicon.hakc.xyz TXT`)

Flag: `SKYLIGHT{dUg_f0r_trE4suRe_x_ic0n_m4rkEd_t#3_sp0t}`
