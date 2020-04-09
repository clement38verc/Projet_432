cas=['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12', 'C13', 'C14', 'C15', 'C16', 'C17', 'C18', 'C19', 'C20', 'C21', 'C22', 'C23', 'C24', 'C25', 'C26', 'C27', 'C28', 'C29', 'C30', 'C31', 'C32', 'C33', 'C34', 'C35', 'C36', 'C37', 'C38', 'C39', 'C40', 'C41', 'C42', 'C43', 'C44', 'C45', 'C46', 'C47', 'C48', 'C49', 'C50', 'C51', 'C52', 'C53', 'C54', 'C55', 'C56', 'C57', 'C58', 'C59', 'C60', 'C61', 'C62', 'C63', 'C64', 'C65', 'C66', 'C67', 'C68', 'C69', 'C70', 'C71', 'C72', 'C73', 'C74', 'C75', 'C76', 'C77', 'C78', 'C79', 'C80', 'C81', 'C82', 'C83', 'C84', 'C85', 'C86', 'C87', 'C88', 'C89', 'C90', 'C91', 'C92', 'C93', 'C94', 'C95', 'C96', 'C97', 'C98', 'C99', 'C100', 'C101', 'C102', 'C103', 'C104', 'C105', 'C106', 'C107', 'C108', 'C109', 'C110', 'C111', 'C112', 'C113', 'C114', 'C115', 'C116', 'C117', 'C118', 'C119', 'C120', 'C121', 'C122', 'C123', 'C124', 'C125', 'C126']

case=['a','b','c','d','e','f','g','h','i']

DNF=['(-a.-b.-c.-d.-e.-f.-g.-h.-i)','(a.-b.-c.-d.-e.-f.-g.-h.-i)+(b.-a.-c.-d.-e.-f.-g.-h.-i)+(c.-a.-b.-d.-e.-f.-g.-h.-i)+(d.-a.-b.-c.-e.-f.-g.-h.-i)+(e.-a.-b.-c.-d.-f.-g.-h.-i)+(f.-a.-b.-c.-d.-e.-g.-h.-i)+(g.-a.-b.-c.-d.-e.-f.-h.-i)+(h.-a.-b.-c.-d.-e.-f.-g.-i)+(i.-a.-b.-c.-d.-e.-f.-g.-h)','(a.b.-c.-d.-e.-f.-g.-h.-i)+(a.c.-b.-d.-e.-f.-g.-h.-i)+(a.d.-b.-c.-e.-f.-g.-h.-i)+(a.e.-b.-c.-d.-f.-g.-h.-i)+(a.f.-b.-c.-d.-e.-g.-h.-i)+(a.g.-b.-c.-d.-e.-f.-h.-i)+(a.h.-b.-c.-d.-e.-f.-g.-i)+(a.i.-b.-c.-d.-e.-f.-g.-h)+(b.c.-a.-d.-e.-f.-g.-h.-i)+(b.d.-a.-c.-e.-f.-g.-h.-i)+(b.e.-a.-c.-d.-f.-g.-h.-i)+(b.f.-a.-c.-d.-e.-g.-h.-i)+(b.g.-a.-c.-d.-e.-f.-h.-i)+(b.h.-a.-c.-d.-e.-f.-g.-i)+(b.i.-a.-c.-d.-e.-f.-g.-h)+(c.d.-a.-b.-e.-f.-g.-h.-i)+(c.e.-a.-b.-d.-f.-g.-h.-i)+(c.f.-a.-b.-d.-e.-g.-h.-i)+(c.g.-a.-b.-d.-e.-f.-h.-i)+(c.h.-a.-b.-d.-e.-f.-g.-i)+(c.i.-a.-b.-d.-e.-f.-g.-h)+(d.e.-a.-b.-c.-f.-g.-h.-i)+(d.f.-a.-b.-c.-e.-g.-h.-i)+(d.g.-a.-b.-c.-e.-f.-h.-i)+(d.h.-a.-b.-c.-e.-f.-g.-i)+(d.i.-a.-b.-c.-e.-f.-g.-h)+(e.f.-a.-b.-c.-d.-g.-h.-i)+(e.g.-a.-b.-c.-d.-f.-h.-i)+(e.h.-a.-b.-c.-d.-f.-g.-i)+(e.i.-a.-b.-c.-d.-f.-g.-h)+(f.g.-a.-b.-c.-d.-e.-h.-i)+(f.h.-a.-b.-c.-d.-e.-g.-i)+(f.i.-a.-b.-c.-d.-e.-g.-h)+(g.h.-a.-b.-c.-d.-e.-f.-i)+(g.i.-a.-b.-c.-d.-e.-f.-h)+(h.i.-a.-b.-c.-d.-e.-f.-g)','(a.b.c.-d.-e.-f.-g.-h.-i)+(a.b.d.-c.-e.-f.-g.-h.-i)+(a.b.e.-c.-d.-f.-g.-h.-i)+(a.b.f.-c.-d.-e.-g.-h.-i)+(a.b.g.-c.-d.-e.-f.-h.-i)+(a.b.h.-c.-d.-e.-f.-g.-i)+(a.b.i.-c.-d.-e.-f.-g.-h)+(a.c.d.-b.-e.-f.-g.-h.-i)+(a.c.e.-b.-d.-f.-g.-h.-i)+(a.c.f.-b.-d.-e.-g.-h.-i)+(a.c.g.-b.-d.-e.-f.-h.-i)+(a.c.h.-b.-d.-e.-f.-g.-i)+(a.c.i.-b.-d.-e.-f.-g.-h)+(a.d.e.-b.-c.-f.-g.-h.-i)+(a.d.f.-b.-c.-e.-g.-h.-i)+(a.d.g.-b.-c.-e.-f.-h.-i)+(a.d.h.-b.-c.-e.-f.-g.-i)+(a.d.i.-b.-c.-e.-f.-g.-h)+(a.e.f.-b.-c.-d.-g.-h.-i)+(a.e.g.-b.-c.-d.-f.-h.-i)+(a.e.h.-b.-c.-d.-f.-g.-i)+(a.e.i.-b.-c.-d.-f.-g.-h)+(a.f.g.-b.-c.-d.-e.-h.-i)+(a.f.h.-b.-c.-d.-e.-g.-i)+(a.f.i.-b.-c.-d.-e.-g.-h)+(a.g.h.-b.-c.-d.-e.-f.-i)+(a.g.i.-b.-c.-d.-e.-f.-h)+(a.h.i.-b.-c.-d.-e.-f.-g)+(b.c.d.-a.-e.-f.-g.-h.-i)+(b.c.e.-a.-d.-f.-g.-h.-i)+(b.c.f.-a.-d.-e.-g.-h.-i)+(b.c.g.-a.-d.-e.-f.-h.-i)+(b.c.h.-a.-d.-e.-f.-g.-i)+(b.c.i.-a.-d.-e.-f.-g.-h)+(b.d.e.-a.-c.-f.-g.-h.-i)+(b.d.f.-a.-c.-e.-g.-h.-i)+(b.d.g.-a.-c.-e.-f.-h.-i)+(b.d.h.-a.-c.-e.-f.-g.-i)+(b.d.i.-a.-c.-e.-f.-g.-h)+(b.e.f.-a.-c.-d.-g.-h.-i)+(b.e.g.-a.-c.-d.-f.-h.-i)+(b.e.h.-a.-c.-d.-f.-g.-i)+(b.e.i.-a.-c.-d.-f.-g.-h)+(b.f.g.-a.-c.-d.-e.-h.-i)+(b.f.h.-a.-c.-d.-e.-g.-i)+(b.f.i.-a.-c.-d.-e.-g.-h)+(b.g.h.-a.-c.-d.-e.-f.-i)+(b.g.i.-a.-c.-d.-e.-f.-h)+(b.h.i.-a.-c.-d.-e.-f.-g)+(c.d.e.-a.-b.-f.-g.-h.-i)+(c.d.f.-a.-b.-e.-g.-h.-i)+(c.d.g.-a.-b.-e.-f.-h.-i)+(c.d.h.-a.-b.-e.-f.-g.-i)+(c.d.i.-a.-b.-e.-f.-g.-h)+(c.e.f.-a.-b.-d.-g.-h.-i)+(c.e.g.-a.-b.-d.-f.-h.-i)+(c.e.h.-a.-b.-d.-f.-g.-i)+(c.e.i.-a.-b.-d.-f.-g.-h)+(c.f.g.-a.-b.-d.-e.-h.-i)+(c.f.h.-a.-b.-d.-e.-g.-i)+(c.f.i.-a.-b.-d.-e.-g.-h)+(c.g.h.-a.-b.-d.-e.-f.-i)+(c.g.i.-a.-b.-d.-e.-f.-h)+(c.h.i.-a.-b.-d.-e.-f.-g)+(d.e.f.-a.-b.-c.-g.-h.-i)+(d.e.g.-a.-b.-c.-f.-h.-i)+(d.e.h.-a.-b.-c.-f.-g.-i)+(d.e.i.-a.-b.-c.-f.-g.-h)+(d.f.g.-a.-b.-c.-e.-h.-i)+(d.f.h.-a.-b.-c.-e.-g.-i)+(d.f.i.-a.-b.-c.-e.-g.-h)+(d.g.h.-a.-b.-c.-e.-f.-i)+(d.g.i.-a.-b.-c.-e.-f.-h)+(d.h.i.-a.-b.-c.-e.-f.-g)+(e.f.g.-a.-b.-c.-d.-h.-i)+(e.f.h.-a.-b.-c.-d.-g.-i)+(e.f.i.-a.-b.-c.-d.-g.-h)+(e.g.h.-a.-b.-c.-d.-f.-i)+(e.g.i.-a.-b.-c.-d.-f.-h)+(e.h.i.-a.-b.-c.-d.-f.-g)+(f.g.h.-a.-b.-c.-d.-e.-i)+(f.g.i.-a.-b.-c.-d.-e.-h)+(f.h.i.-a.-b.-c.-d.-e.-g)+(g.h.i.-a.-b.-c.-d.-e.-f)','(a.b.c.d.-e.-f.-g.-h.-i)+(a.b.c.e.-d.-f.-g.-h.-i)+(a.b.c.f.-d.-e.-g.-h.-i)+(a.b.c.g.-d.-e.-f.-h.-i)+(a.b.c.h.-d.-e.-f.-g.-i)+(a.b.c.i.-d.-e.-f.-g.-h)+(a.b.d.e.-c.-f.-g.-h.-i)+(a.b.d.f.-c.-e.-g.-h.-i)+(a.b.d.g.-c.-e.-f.-h.-i)+(a.b.d.h.-c.-e.-f.-g.-i)+(a.b.d.i.-c.-e.-f.-g.-h)+(a.b.e.f.-c.-d.-g.-h.-i)+(a.b.e.g.-c.-d.-f.-h.-i)+(a.b.e.h.-c.-d.-f.-g.-i)+(a.b.e.i.-c.-d.-f.-g.-h)+(a.b.f.g.-c.-d.-e.-h.-i)+(a.b.f.h.-c.-d.-e.-g.-i)+(a.b.f.i.-c.-d.-e.-g.-h)+(a.b.g.h.-c.-d.-e.-f.-i)+(a.b.g.i.-c.-d.-e.-f.-h)+(a.b.h.i.-c.-d.-e.-f.-g)+(a.c.d.e.-b.-f.-g.-h.-i)+(a.c.d.f.-b.-e.-g.-h.-i)+(a.c.d.g.-b.-e.-f.-h.-i)+(a.c.d.h.-b.-e.-f.-g.-i)+(a.c.d.i.-b.-e.-f.-g.-h)+(a.c.e.f.-b.-d.-g.-h.-i)+(a.c.e.g.-b.-d.-f.-h.-i)+(a.c.e.h.-b.-d.-f.-g.-i)+(a.c.e.i.-b.-d.-f.-g.-h)+(a.c.f.g.-b.-d.-e.-h.-i)+(a.c.f.h.-b.-d.-e.-g.-i)+(a.c.f.i.-b.-d.-e.-g.-h)+(a.c.g.h.-b.-d.-e.-f.-i)+(a.c.g.i.-b.-d.-e.-f.-h)+(a.c.h.i.-b.-d.-e.-f.-g)+(a.d.e.f.-b.-c.-g.-h.-i)+(a.d.e.g.-b.-c.-f.-h.-i)+(a.d.e.h.-b.-c.-f.-g.-i)+(a.d.e.i.-b.-c.-f.-g.-h)+(a.d.f.g.-b.-c.-e.-h.-i)+(a.d.f.h.-b.-c.-e.-g.-i)+(a.d.f.i.-b.-c.-e.-g.-h)+(a.d.g.h.-b.-c.-e.-f.-i)+(a.d.g.i.-b.-c.-e.-f.-h)+(a.d.h.i.-b.-c.-e.-f.-g)+(a.e.f.g.-b.-c.-d.-h.-i)+(a.e.f.h.-b.-c.-d.-g.-i)+(a.e.f.i.-b.-c.-d.-g.-h)+(a.e.g.h.-b.-c.-d.-f.-i)+(a.e.g.i.-b.-c.-d.-f.-h)+(a.e.h.i.-b.-c.-d.-f.-g)+(a.f.g.h.-b.-c.-d.-e.-i)+(a.f.g.i.-b.-c.-d.-e.-h)+(a.f.h.i.-b.-c.-d.-e.-g)+(a.g.h.i.-b.-c.-d.-e.-f)+(b.c.d.e.-a.-f.-g.-h.-i)+(b.c.d.f.-a.-e.-g.-h.-i)+(b.c.d.g.-a.-e.-f.-h.-i)+(b.c.d.h.-a.-e.-f.-g.-i)+(b.c.d.i.-a.-e.-f.-g.-h)+(b.c.e.f.-a.-d.-g.-h.-i)+(b.c.e.g.-a.-d.-f.-h.-i)+(b.c.e.h.-a.-d.-f.-g.-i)+(b.c.e.i.-a.-d.-f.-g.-h)+(b.c.f.g.-a.-d.-e.-h.-i)+(b.c.f.h.-a.-d.-e.-g.-i)+(b.c.f.i.-a.-d.-e.-g.-h)+(b.c.g.h.-a.-d.-e.-f.-i)+(b.c.g.i.-a.-d.-e.-f.-h)+(b.c.h.i.-a.-d.-e.-f.-g)+(b.d.e.f.-a.-c.-g.-h.-i)+(b.d.e.g.-a.-c.-f.-h.-i)+(b.d.e.h.-a.-c.-f.-g.-i)+(b.d.e.i.-a.-c.-f.-g.-h)+(b.d.f.g.-a.-c.-e.-h.-i)+(b.d.f.h.-a.-c.-e.-g.-i)+(b.d.f.i.-a.-c.-e.-g.-h)+(b.d.g.h.-a.-c.-e.-f.-i)+(b.d.g.i.-a.-c.-e.-f.-h)+(b.d.h.i.-a.-c.-e.-f.-g)+(b.e.f.g.-a.-c.-d.-h.-i)+(b.e.f.h.-a.-c.-d.-g.-i)+(b.e.f.i.-a.-c.-d.-g.-h)+(b.e.g.h.-a.-c.-d.-f.-i)+(b.e.g.i.-a.-c.-d.-f.-h)+(b.e.h.i.-a.-c.-d.-f.-g)+(b.f.g.h.-a.-c.-d.-e.-i)+(b.f.g.i.-a.-c.-d.-e.-h)+(b.f.h.i.-a.-c.-d.-e.-g)+(b.g.h.i.-a.-c.-d.-e.-f)+(c.d.e.f.-a.-b.-g.-h.-i)+(c.d.e.g.-a.-b.-f.-h.-i)+(c.d.e.h.-a.-b.-f.-g.-i)+(c.d.e.i.-a.-b.-f.-g.-h)+(c.d.f.g.-a.-b.-e.-h.-i)+(c.d.f.h.-a.-b.-e.-g.-i)+(c.d.f.i.-a.-b.-e.-g.-h)+(c.d.g.h.-a.-b.-e.-f.-i)+(c.d.g.i.-a.-b.-e.-f.-h)+(c.d.h.i.-a.-b.-e.-f.-g)+(c.e.f.g.-a.-b.-d.-h.-i)+(c.e.f.h.-a.-b.-d.-g.-i)+(c.e.f.i.-a.-b.-d.-g.-h)+(c.e.g.h.-a.-b.-d.-f.-i)+(c.e.g.i.-a.-b.-d.-f.-h)+(c.e.h.i.-a.-b.-d.-f.-g)+(c.f.g.h.-a.-b.-d.-e.-i)+(c.f.g.i.-a.-b.-d.-e.-h)+(c.f.h.i.-a.-b.-d.-e.-g)+(c.g.h.i.-a.-b.-d.-e.-f)+(d.e.f.g.-a.-b.-c.-h.-i)+(d.e.f.h.-a.-b.-c.-g.-i)+(d.e.f.i.-a.-b.-c.-g.-h)+(d.e.g.h.-a.-b.-c.-f.-i)+(d.e.g.i.-a.-b.-c.-f.-h)+(d.e.h.i.-a.-b.-c.-f.-g)+(d.f.g.h.-a.-b.-c.-e.-i)+(d.f.g.i.-a.-b.-c.-e.-h)+(d.f.h.i.-a.-b.-c.-e.-g)+(d.g.h.i.-a.-b.-c.-e.-f)+(e.f.g.h.-a.-b.-c.-d.-i)+(e.f.g.i.-a.-b.-c.-d.-h)+(e.f.h.i.-a.-b.-c.-d.-g)+(e.g.h.i.-a.-b.-c.-d.-f)+(f.g.h.i.-a.-b.-c.-d.-e)','(-a.-b.-c.-d.e.f.g.h.i)+(-a.-b.-c.-e.d.f.g.h.i)+(-a.-b.-c.-f.d.e.g.h.i)+(-a.-b.-c.-g.d.e.f.h.i)+(-a.-b.-c.-h.d.e.f.g.i)+(-a.-b.-c.-i.d.e.f.g.h)+(-a.-b.-d.-e.c.f.g.h.i)+(-a.-b.-d.-f.c.e.g.h.i)+(-a.-b.-d.-g.c.e.f.h.i)+(-a.-b.-d.-h.c.e.f.g.i)+(-a.-b.-d.-i.c.e.f.g.h)+(-a.-b.-e.-f.c.d.g.h.i)+(-a.-b.-e.-g.c.d.f.h.i)+(-a.-b.-e.-h.c.d.f.g.i)+(-a.-b.-e.-i.c.d.f.g.h)+(-a.-b.-f.-g.c.d.e.h.i)+(-a.-b.-f.-h.c.d.e.g.i)+(-a.-b.-f.-i.c.d.e.g.h)+(-a.-b.-g.-h.c.d.e.f.i)+(-a.-b.-g.-i.c.d.e.f.h)+(-a.-b.-h.-i.c.d.e.f.g)+(-a.-c.-d.-e.b.f.g.h.i)+(-a.-c.-d.-f.b.e.g.h.i)+(-a.-c.-d.-g.b.e.f.h.i)+(-a.-c.-d.-h.b.e.f.g.i)+(-a.-c.-d.-i.b.e.f.g.h)+(-a.-c.-e.-f.b.d.g.h.i)+(-a.-c.-e.-g.b.d.f.h.i)+(-a.-c.-e.-h.b.d.f.g.i)+(-a.-c.-e.-i.b.d.f.g.h)+(-a.-c.-f.-g.b.d.e.h.i)+(-a.-c.-f.-h.b.d.e.g.i)+(-a.-c.-f.-i.b.d.e.g.h)+(-a.-c.-g.-h.b.d.e.f.i)+(-a.-c.-g.-i.b.d.e.f.h)+(-a.-c.-h.-i.b.d.e.f.g)+(-a.-d.-e.-f.b.c.g.h.i)+(-a.-d.-e.-g.b.c.f.h.i)+(-a.-d.-e.-h.b.c.f.g.i)+(-a.-d.-e.-i.b.c.f.g.h)+(-a.-d.-f.-g.b.c.e.h.i)+(-a.-d.-f.-h.b.c.e.g.i)+(-a.-d.-f.-i.b.c.e.g.h)+(-a.-d.-g.-h.b.c.e.f.i)+(-a.-d.-g.-i.b.c.e.f.h)+(-a.-d.-h.-i.b.c.e.f.g)+(-a.-e.-f.-g.b.c.d.h.i)+(-a.-e.-f.-h.b.c.d.g.i)+(-a.-e.-f.-i.b.c.d.g.h)+(-a.-e.-g.-h.b.c.d.f.i)+(-a.-e.-g.-i.b.c.d.f.h)+(-a.-e.-h.-i.b.c.d.f.g)+(-a.-f.-g.-h.b.c.d.e.i)+(-a.-f.-g.-i.b.c.d.e.h)+(-a.-f.-h.-i.b.c.d.e.g)+(-a.-g.-h.-i.b.c.d.e.f)+(-b.-c.-d.-e.a.f.g.h.i)+(-b.-c.-d.-f.a.e.g.h.i)+(-b.-c.-d.-g.a.e.f.h.i)+(-b.-c.-d.-h.a.e.f.g.i)+(-b.-c.-d.-i.a.e.f.g.h)+(-b.-c.-e.-f.a.d.g.h.i)+(-b.-c.-e.-g.a.d.f.h.i)+(-b.-c.-e.-h.a.d.f.g.i)+(-b.-c.-e.-i.a.d.f.g.h)+(-b.-c.-f.-g.a.d.e.h.i)+(-b.-c.-f.-h.a.d.e.g.i)+(-b.-c.-f.-i.a.d.e.g.h)+(-b.-c.-g.-h.a.d.e.f.i)+(-b.-c.-g.-i.a.d.e.f.h)+(-b.-c.-h.-i.a.d.e.f.g)+(-b.-d.-e.-f.a.c.g.h.i)+(-b.-d.-e.-g.a.c.f.h.i)+(-b.-d.-e.-h.a.c.f.g.i)+(-b.-d.-e.-i.a.c.f.g.h)+(-b.-d.-f.-g.a.c.e.h.i)+(-b.-d.-f.-h.a.c.e.g.i)+(-b.-d.-f.-i.a.c.e.g.h)+(-b.-d.-g.-h.a.c.e.f.i)+(-b.-d.-g.-i.a.c.e.f.h)+(-b.-d.-h.-i.a.c.e.f.g)+(-b.-e.-f.-g.a.c.d.h.i)+(-b.-e.-f.-h.a.c.d.g.i)+(-b.-e.-f.-i.a.c.d.g.h)+(-b.-e.-g.-h.a.c.d.f.i)+(-b.-e.-g.-i.a.c.d.f.h)+(-b.-e.-h.-i.a.c.d.f.g)+(-b.-f.-g.-h.a.c.d.e.i)+(-b.-f.-g.-i.a.c.d.e.h)+(-b.-f.-h.-i.a.c.d.e.g)+(-b.-g.-h.-i.a.c.d.e.f)+(-c.-d.-e.-f.a.b.g.h.i)+(-c.-d.-e.-g.a.b.f.h.i)+(-c.-d.-e.-h.a.b.f.g.i)+(-c.-d.-e.-i.a.b.f.g.h)+(-c.-d.-f.-g.a.b.e.h.i)+(-c.-d.-f.-h.a.b.e.g.i)+(-c.-d.-f.-i.a.b.e.g.h)+(-c.-d.-g.-h.a.b.e.f.i)+(-c.-d.-g.-i.a.b.e.f.h)+(-c.-d.-h.-i.a.b.e.f.g)+(-c.-e.-f.-g.a.b.d.h.i)+(-c.-e.-f.-h.a.b.d.g.i)+(-c.-e.-f.-i.a.b.d.g.h)+(-c.-e.-g.-h.a.b.d.f.i)+(-c.-e.-g.-i.a.b.d.f.h)+(-c.-e.-h.-i.a.b.d.f.g)+(-c.-f.-g.-h.a.b.d.e.i)+(-c.-f.-g.-i.a.b.d.e.h)+(-c.-f.-h.-i.a.b.d.e.g)+(-c.-g.-h.-i.a.b.d.e.f)+(-d.-e.-f.-g.a.b.c.h.i)+(-d.-e.-f.-h.a.b.c.g.i)+(-d.-e.-f.-i.a.b.c.g.h)+(-d.-e.-g.-h.a.b.c.f.i)+(-d.-e.-g.-i.a.b.c.f.h)+(-d.-e.-h.-i.a.b.c.f.g)+(-d.-f.-g.-h.a.b.c.e.i)+(-d.-f.-g.-i.a.b.c.e.h)+(-d.-f.-h.-i.a.b.c.e.g)+(-d.-g.-h.-i.a.b.c.e.f)+(-e.-f.-g.-h.a.b.c.d.i)+(-e.-f.-g.-i.a.b.c.d.h)+(-e.-f.-h.-i.a.b.c.d.g)+(-e.-g.-h.-i.a.b.c.d.f)+(-f.-g.-h.-i.a.b.c.d.e)','(-a.-b.-c.d.e.f.g.h.i)+(-a.-b.-d.c.e.f.g.h.i)+(-a.-b.-e.c.d.f.g.h.i)+(-a.-b.-f.c.d.e.g.h.i)+(-a.-b.-g.c.d.e.f.h.i)+(-a.-b.-h.c.d.e.f.g.i)+(-a.-b.-i.c.d.e.f.g.h)+(-a.-c.-d.b.e.f.g.h.i)+(-a.-c.-e.b.d.f.g.h.i)+(-a.-c.-f.b.d.e.g.h.i)+(-a.-c.-g.b.d.e.f.h.i)+(-a.-c.-h.b.d.e.f.g.i)+(-a.-c.-i.b.d.e.f.g.h)+(-a.-d.-e.b.c.f.g.h.i)+(-a.-d.-f.b.c.e.g.h.i)+(-a.-d.-g.b.c.e.f.h.i)+(-a.-d.-h.b.c.e.f.g.i)+(-a.-d.-i.b.c.e.f.g.h)+(-a.-e.-f.b.c.d.g.h.i)+(-a.-e.-g.b.c.d.f.h.i)+(-a.-e.-h.b.c.d.f.g.i)+(-a.-e.-i.b.c.d.f.g.h)+(-a.-f.-g.b.c.d.e.h.i)+(-a.-f.-h.b.c.d.e.g.i)+(-a.-f.-i.b.c.d.e.g.h)+(-a.-g.-h.b.c.d.e.f.i)+(-a.-g.-i.b.c.d.e.f.h)+(-a.-h.-i.b.c.d.e.f.g)+(-b.-c.-d.a.e.f.g.h.i)+(-b.-c.-e.a.d.f.g.h.i)+(-b.-c.-f.a.d.e.g.h.i)+(-b.-c.-g.a.d.e.f.h.i)+(-b.-c.-h.a.d.e.f.g.i)+(-b.-c.-i.a.d.e.f.g.h)+(-b.-d.-e.a.c.f.g.h.i)+(-b.-d.-f.a.c.e.g.h.i)+(-b.-d.-g.a.c.e.f.h.i)+(-b.-d.-h.a.c.e.f.g.i)+(-b.-d.-i.a.c.e.f.g.h)+(-b.-e.-f.a.c.d.g.h.i)+(-b.-e.-g.a.c.d.f.h.i)+(-b.-e.-h.a.c.d.f.g.i)+(-b.-e.-i.a.c.d.f.g.h)+(-b.-f.-g.a.c.d.e.h.i)+(-b.-f.-h.a.c.d.e.g.i)+(-b.-f.-i.a.c.d.e.g.h)+(-b.-g.-h.a.c.d.e.f.i)+(-b.-g.-i.a.c.d.e.f.h)+(-b.-h.-i.a.c.d.e.f.g)+(-c.-d.-e.a.b.f.g.h.i)+(-c.-d.-f.a.b.e.g.h.i)+(-c.-d.-g.a.b.e.f.h.i)+(-c.-d.-h.a.b.e.f.g.i)+(-c.-d.-i.a.b.e.f.g.h)+(-c.-e.-f.a.b.d.g.h.i)+(-c.-e.-g.a.b.d.f.h.i)+(-c.-e.-h.a.b.d.f.g.i)+(-c.-e.-i.a.b.d.f.g.h)+(-c.-f.-g.a.b.d.e.h.i)+(-c.-f.-h.a.b.d.e.g.i)+(-c.-f.-i.a.b.d.e.g.h)+(-c.-g.-h.a.b.d.e.f.i)+(-c.-g.-i.a.b.d.e.f.h)+(-c.-h.-i.a.b.d.e.f.g)+(-d.-e.-f.a.b.c.g.h.i)+(-d.-e.-g.a.b.c.f.h.i)+(-d.-e.-h.a.b.c.f.g.i)+(-d.-e.-i.a.b.c.f.g.h)+(-d.-f.-g.a.b.c.e.h.i)+(-d.-f.-h.a.b.c.e.g.i)+(-d.-f.-i.a.b.c.e.g.h)+(-d.-g.-h.a.b.c.e.f.i)+(-d.-g.-i.a.b.c.e.f.h)+(-d.-h.-i.a.b.c.e.f.g)+(-e.-f.-g.a.b.c.d.h.i)+(-e.-f.-h.a.b.c.d.g.i)+(-e.-f.-i.a.b.c.d.g.h)+(-e.-g.-h.a.b.c.d.f.i)+(-e.-g.-i.a.b.c.d.f.h)+(-e.-h.-i.a.b.c.d.f.g)+(-f.-g.-h.a.b.c.d.e.i)+(-f.-g.-i.a.b.c.d.e.h)+(-f.-h.-i.a.b.c.d.e.g)+(-g.-h.-i.a.b.c.d.e.f)','(-a.-b.c.d.e.f.g.h.i)+(-a.-c.b.d.e.f.g.h.i)+(-a.-d.b.c.e.f.g.h.i)+(-a.-e.b.c.d.f.g.h.i)+(-a.-f.b.c.d.e.g.h.i)+(-a.-g.b.c.d.e.f.h.i)+(-a.-h.b.c.d.e.f.g.i)+(-a.-i.b.c.d.e.f.g.h)+(-b.-c.a.d.e.f.g.h.i)+(-b.-d.a.c.e.f.g.h.i)+(-b.-e.a.c.d.f.g.h.i)+(-b.-f.a.c.d.e.g.h.i)+(-b.-g.a.c.d.e.f.h.i)+(-b.-h.a.c.d.e.f.g.i)+(-b.-i.a.c.d.e.f.g.h)+(-c.-d.a.b.e.f.g.h.i)+(-c.-e.a.b.d.f.g.h.i)+(-c.-f.a.b.d.e.g.h.i)+(-c.-g.a.b.d.e.f.h.i)+(-c.-h.a.b.d.e.f.g.i)+(-c.-i.a.b.d.e.f.g.h)+(-d.-e.a.b.c.f.g.h.i)+(-d.-f.a.b.c.e.g.h.i)+(-d.-g.a.b.c.e.f.h.i)+(-d.-h.a.b.c.e.f.g.i)+(-d.-i.a.b.c.e.f.g.h)+(-e.-f.a.b.c.d.g.h.i)+(-e.-g.a.b.c.d.f.h.i)+(-e.-h.a.b.c.d.f.g.i)+(-e.-i.a.b.c.d.f.g.h)+(-f.-g.a.b.c.d.e.h.i)+(-f.-h.a.b.c.d.e.g.i)+(-f.-i.a.b.c.d.e.g.h)+(-g.-h.a.b.c.d.e.f.i)+(-g.-i.a.b.c.d.e.f.h)+(-h.-i.a.b.c.d.e.f.g)','(-a.b.c.d.e.f.g.h.i)+(-b.a.c.d.e.f.g.h.i)+(-c.a.b.d.e.f.g.h.i)+(-d.a.b.c.e.f.g.h.i)+(-e.a.b.c.d.f.g.h.i)+(-f.a.b.c.d.e.g.h.i)+(-g.a.b.c.d.e.f.h.i)+(-h.a.b.c.d.e.f.g.i)+(-i.a.b.c.d.e.f.g.h)','(a.b.c.d.e.f.g.h.i)']

def dnf_cnf(dnf):
    cnf=dict()
    cnf["0"]=dnf[0]
    for i in range(1,9):
        k=0
        ch="("
        ch1="(C1"
        for el in dnf[i]:
            if (el=="+"):
                k+=1
                ch1=ch1+"."+cas[k]
            if (el=="a"):
                ch=ch+el+"+-"+cas[k]+").("
            if (el=="b"):
                ch=ch+el+"+-"+cas[k]+").("
            if (el=="c"):
                ch=ch+el+"+-"+cas[k]+").("
            if (el=="d"):
                ch=ch+el+"+-"+cas[k]+").("
            if (el=="e"):
                ch=ch+el+"+-"+cas[k]+").("
            if (el=="f"):
                ch=ch+el+"+-"+cas[k]+").("
            if (el=="g"):
                ch=ch+el+"+-"+cas[k]+").("
            if (el=="h"):
                ch=ch+el+"+-"+cas[k]+").("
            if (el=="i"):
                ch=ch+el+"+-"+cas[k]+").("
            if (el=="-"):
                ch=ch+"-"
        k+=1
        ch=ch+")."+ch1+")."
        for m in range(k):
            for n in range(m+1,k):
                ch=ch+"(-"+cas[m]+"+-"+cas[n]+")"
                if ((m!=8) or (n!=9)):
                    ch=ch+"."
        cnf[str(i)]=ch
    cnf["9"]=dnf[9]
    return cnf

def crea_cnf(grille,cnf):
    ch=""
    clauses=0
    for i in range(len(grille)):
        for j in range(len(grille)):
            if (grille[i,j]==0):
                ch=ch+cnf.get("0")
                clauses+=1
            if (grille[i,j]==1):
                ch=ch+cnf.get("1")
                clauses+=118
            if (grille[i,j]==2):
                ch=ch+cnf.get("2")
                clauses+=955
            if (grille[i,j]==3):
                ch=ch+cnf.get("3")
                clauses+=4243
            if (grille[i,j]==4):
                ch=ch+cnf.get("4")
                clauses+=9010
            if (grille[i,j]==5):
                ch=ch+cnf.get("5")
                clauses+=9010
            if (grille[i,j]==6):
                ch=ch+cnf.get("6")
                clauses+=4243
            if (grille[i,j]==7):
                ch=ch+cnf.get("7")
                clauses+=955
            if (grille[i,j]==8):
                ch=ch+cnf.get("8")
                clauses+=118
            if (grille[i,j]==9):
                ch=ch+cnf.get("9")
                clauses+=1
            if ((i!=len(grille)-1) or (j!=len(grille)-1)):
                ch=ch+"."
    return (ch,clauses)

