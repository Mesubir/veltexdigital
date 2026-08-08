import subprocess
import sys

def publish():
    print("=========================================")
    print("   PUBLISHING TO GITHUB REPOSITORY")
    print("   Target: https://github.com/Mesubir/veltexdigital (branch: main)")
    print("=========================================\n")
    
    try:
        # Step 1: Git Add
        print("[1/3] Staging changes...")
        res_add = subprocess.run(["git", "add", "."], capture_output=True, text=True)
        print(res_add.stdout)
        if res_add.stderr:
            print(res_add.stderr)
            
        # Step 2: Git Commit
        print("[2/3] Creating commit...")
        commit_msg = "feat: Add SEO blog hub, structured articles, humanized guides, and site navigation updates"
        res_commit = subprocess.run(["git", "commit", "-m", commit_msg], capture_output=True, text=True)
        print(res_commit.stdout)
        if res_commit.stderr:
            print(res_commit.stderr)
            
        # Step 3: Git Push
        print("[3/3] Pushing to GitHub (main branch)...")
        res_push = subprocess.run(["git", "push", "-u", "origin", "main"], capture_output=True, text=True)
        print(res_push.stdout)
        if res_push.stderr:
            print(res_push.stderr)
            
        print("\n✅ Publishing complete! View your deployed website repository at:")
        print("   https://github.com/Mesubir/veltexdigital")
        
    except Exception as e:
        print(f"❌ Error during publication: {e}")

if __name__ == "__main__":
    publish()
