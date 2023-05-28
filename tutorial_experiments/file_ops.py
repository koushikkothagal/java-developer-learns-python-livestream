with open('../TODO.md', encoding='utf-8') as f:
    
        print(f.read(5))
        print(f'****** {f.tell()} *******')
        print(f.read(5))
        print(f'****** {f.tell()} *******')
        print(f.read(5))
        print(f'****** {f.tell()} *******')
        

# with open('../python_brains_channel_ideas.md', 'w', encoding='utf-8') as f:
#     pass