hD, mD = input("entrez heure de début: ").split(":")
hF, mF = input("entrez heure de fin: ").split(":")
p = input("entrez temps de pause (en minutes): ")
hD = int(hD)
mD = int(mD)
hF = int(hF)
mF = int(mF)
p = int(p)
if (hD > 23) or (hF > 23) or (mD > 59) or (mF > 59):
    print("Heure non valide")
else:
    if hD > hF:
        hF = hF + 24
    if mD > mF:
        hF = hF - 1
        mF = mF + 60
    if p > 59:
        hF = hF - int(p/60)
        p = p % 60
    h_res = hF - hD
    m_res = (mF - mD) - p
    if (m_res < 0):
        h_res = h_res - 1
        m_res = m_res + 60
    if (h_res < 10):
        h_res = str(h_res)
        h_res = "0" + h_res
    if (m_res < 10):
        m_res = str(m_res)
        m_res = "0" + m_res
    else:
        h_res = str(h_res)
        m_res = str(m_res)
    print(h_res, ":", m_res)
