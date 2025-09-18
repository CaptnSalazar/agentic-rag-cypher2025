from orchestrator import AgenticRAG

if __name__ == '__main__':
    q = input('Enter query: ')
    ag = AgenticRAG()
    out = ag.handle(q)
    import json
    print('\n--- FINAL ANSWER ---\n')
    print(out.get('answer'))
    print('\n--- PROVENANCE ---\n')
    for p in out.get('provenance', []):
        print(p)
    if out.get('verification'):
        print('\n--- VERIFICATION ---\n')
        print(out['verification'])
    if out.get('reasoning'):
        print('\n--- REASONING STEPS ---\n')
        for s in out['reasoning']['steps']:
            print('-', s)
        print('\nConclusion:', out['reasoning']['conclusion'])