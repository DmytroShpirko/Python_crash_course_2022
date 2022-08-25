# CHAPTER 2

## Ex 2-1


~~~
message = "Test text message"
print(message)
~~~

~~~
tgk-25:Python_Crash_Course_2022 tgk$ python3 Chapter2/simple_message.py
Test text message
~~~

## Ex 2-2

~~~
message = "First test text message"
print(message)
message = "Second test text message"
print(message)
~~~

~~~
tgk-25:Python_Crash_Course_2022 tgk$ python3 Chapter2/simple_messages.py
First test text message
Second test text message
~~~

## Ex 2-3

~~~
name = "Dmytro"
print ("Hello, " + name.title() +  ", would you like to learn some Python today")
~~~

~~~
tgk-25:Python_Crash_Course_2022 tgk$ python3 Chapter2/name_cases2-3.py
Hello, Dmytro, would you like to learn some Python today
~~~

## Ex 2-4

~~~
name = "dmytro yaroslavovych shpirko"
print (name.lower())
print (name.upper())
print (name.title ())
~~~

~~~
tgk-25:Python_Crash_Course_2022 tgk$ python3 Chapter2/name_cases2-4.py
dmytro yaroslavovych shpirko
DMYTRO YAROSLAVOVYCH SHPIRKO
Dmytro Yaroslavovych Shpirko
~~~

## Ex 2-5

~~~
print ('British writer Edmund Burke said: "You can never plan the future by the past"')
~~~

~~~
tgk-25:Python_Crash_Course_2022 tgk$ python3 Chapter2/name_cases2-5.py
British writer Edmund Burke said: "You can never plan the future by the past"
~~~

## Ex 2-6

~~~
famous_person="Edmund Burke"
message = "British writer " + famous_person.title() + " said: 'You can never plan the future by the past'"
print (message)
~~~

~~~
tgk-25:Python_Crash_Course_2022 tgk$ python3 Chapter2/name_cases2-6.py
British writer Edmund Burke said: 'You can never plan the future by the past'
~~~

## Ex 2-7

~~~
name ="  Dmytro\n Yaroslavovych\n\t Shpirko\t "
print (name)
print (name.rstrip())
print (name.lstrip())
print (name.strip())
~~~

~~~
tgk-25:Python_Crash_Course_2022 tgk$ python3 Chapter2/name_cases2-7.py
  Dmytro
 Yaroslavovych
         Shpirko         
  Dmytro
 Yaroslavovych
         Shpirko
Dmytro
 Yaroslavovych
         Shpirko         
Dmytro
 Yaroslavovych
         Shpirko
~~~

## Ex 2-8

~~~
print (5 + 3)
print (8 - 0)
print (9 - 1)
print (4 * 2)
~~~

~~~
8
8
8
8
~~~


## Ex 2-9

~~~
#inform about favourite number
number ="13"
message = "I know that " + str (number) + " is your favourite number"
print (message)
~~~

~~~
tgk-25:Python_Crash_Course_2022 tgk$ python3 Chapter2/calcul_cases2-9.py
I know that 13 is your favourite number
~~~

